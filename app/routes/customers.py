from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Customer
from ..schemas import CustomerCreate, CustomerResponse, CustomerUpdate

router = APIRouter(tags=["customers"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/customers", response_model=CustomerResponse)
def create_customer(data: CustomerCreate, db: Session = Depends(get_db)):
    customer = Customer(
        name=data.name,
        street=data.street,
        zip_code=data.zip_code,
        city=data.city,
        phone=data.phone,
        email=data.email,
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


@router.get("/customers", response_model=list[CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    return db.query(Customer).order_by(Customer.id.desc()).all()


@router.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Kunde nicht gefunden.")
    return customer


@router.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, data: CustomerUpdate, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Kunde nicht gefunden.")

    customer.name = data.name
    customer.street = data.street
    customer.zip_code = data.zip_code
    customer.city = data.city
    customer.phone = data.phone
    customer.email = data.email

    db.commit()
    db.refresh(customer)
    return customer


@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Kunde nicht gefunden.")

    db.delete(customer)
    db.commit()
    return {"message": "Kunde gelöscht"}
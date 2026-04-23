from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from ..database import SessionLocal
from ..models import Customer, JobReport, MaterialItem
from ..schemas import (
    JobReportCreate,
    JobReportResponse,
    JobReportListResponse,
    JobReportUpdate,
)
from ..services.pricing import (
    calculate_labor_minutes,
    calculate_labor_cost,
    calculate_material_total,
    calculate_total_cost,
)

router = APIRouter(tags=["job_reports"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/job-reports", response_model=JobReportResponse)
def create_job_report(data: JobReportCreate, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == data.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Kunde nicht gefunden.")

    try:
        labor_minutes = calculate_labor_minutes(data.start_time, data.end_time)
        labor_cost = calculate_labor_cost(labor_minutes, data.hourly_rate)

        material_items = []
        material_cost = 0.0

        for item in data.materials:
            total_price = calculate_material_total(item.quantity, item.unit_price)
            material_cost += total_price

            material_items.append(
                MaterialItem(
                    name=item.name,
                    quantity=item.quantity,
                    unit=item.unit,
                    unit_price=item.unit_price,
                    total_price=total_price,
                )
            )

        material_cost = round(material_cost, 2)
        total_cost = calculate_total_cost(labor_cost, material_cost, data.travel_cost)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    report = JobReport(
        customer_id=data.customer_id,
        work_date=data.work_date,
        start_time=data.start_time,
        end_time=data.end_time,
        description=data.description,
        notes=data.notes,
        hourly_rate=data.hourly_rate,
        travel_cost=data.travel_cost,
        labor_minutes=labor_minutes,
        labor_cost=labor_cost,
        material_cost=material_cost,
        total_cost=total_cost,
        materials=material_items,
    )

    db.add(report)
    db.commit()
    db.refresh(report)
    return report


@router.get("/job-reports", response_model=list[JobReportListResponse])
def list_job_reports(db: Session = Depends(get_db)):
    reports = (
        db.query(JobReport)
        .options(joinedload(JobReport.customer))
        .order_by(JobReport.id.desc())
        .all()
    )

    result = []
    for report in reports:
        result.append({
            "id": report.id,
            "customer_id": report.customer_id,
            "customer_name": report.customer.name if report.customer else None,
            "work_date": report.work_date,
            "total_cost": report.total_cost,
            "created_at": report.created_at,
        })

    return result


@router.get("/job-reports/{report_id}", response_model=JobReportResponse)
def get_job_report(report_id: int, db: Session = Depends(get_db)):
    report = (
        db.query(JobReport)
        .options(joinedload(JobReport.materials), joinedload(JobReport.customer))
        .filter(JobReport.id == report_id)
        .first()
    )

    if not report:
        raise HTTPException(status_code=404, detail="Bericht nicht gefunden.")

    return report


@router.put("/job-reports/{report_id}", response_model=JobReportResponse)
def update_job_report(report_id: int, data: JobReportUpdate, db: Session = Depends(get_db)):
    report = db.query(JobReport).filter(JobReport.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Bericht nicht gefunden.")

    customer = db.query(Customer).filter(Customer.id == data.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Kunde nicht gefunden.")

    try:
        labor_minutes = calculate_labor_minutes(data.start_time, data.end_time)
        labor_cost = calculate_labor_cost(labor_minutes, data.hourly_rate)

        material_items = []
        material_cost = 0.0

        for item in data.materials:
            total_price = calculate_material_total(item.quantity, item.unit_price)
            material_cost += total_price

            material_items.append(
                MaterialItem(
                    name=item.name,
                    quantity=item.quantity,
                    unit=item.unit,
                    unit_price=item.unit_price,
                    total_price=total_price,
                )
            )

        material_cost = round(material_cost, 2)
        total_cost = calculate_total_cost(labor_cost, material_cost, data.travel_cost)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    report.customer_id = data.customer_id
    report.work_date = data.work_date
    report.start_time = data.start_time
    report.end_time = data.end_time
    report.description = data.description
    report.notes = data.notes
    report.hourly_rate = data.hourly_rate
    report.travel_cost = data.travel_cost
    report.labor_minutes = labor_minutes
    report.labor_cost = labor_cost
    report.material_cost = material_cost
    report.total_cost = total_cost

    report.materials.clear()
    for item in material_items:
        report.materials.append(item)

    db.commit()
    db.refresh(report)
    return report


@router.delete("/job-reports/{report_id}")
def delete_job_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(JobReport).filter(JobReport.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Bericht nicht gefunden.")

    db.delete(report)
    db.commit()
    return {"message": "Bericht gelöscht"}
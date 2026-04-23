from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime, date


class CustomerCreate(BaseModel):
    name: str
    street: str
    zip_code: str
    city: str
    phone: str
    email: Optional[EmailStr] = None


class CustomerResponse(BaseModel):
    id: int
    name: str
    street: str
    zip_code: str
    city: str
    phone: str
    email: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class MaterialItemCreate(BaseModel):
    name: str
    quantity: float
    unit: str
    unit_price: float


class MaterialItemResponse(BaseModel):
    id: int
    name: str
    quantity: float
    unit: str
    unit_price: float
    total_price: float

    class Config:
        from_attributes = True


class JobReportCreate(BaseModel):
    customer_id: int
    work_date: date
    start_time: str
    end_time: str
    description: str
    notes: Optional[str] = None
    hourly_rate: float
    travel_cost: float = 0
    materials: List[MaterialItemCreate]

class JobReportListResponse(BaseModel):
    id: int
    customer_id: int
    customer_name: str | None = None
    work_date: date
    total_cost: float
    created_at: datetime

    class Config:
        from_attributes = True


class JobReportResponse(BaseModel):
    id: int
    customer_id: int
    work_date: date
    start_time: str
    end_time: str
    description: str
    notes: Optional[str] = None
    hourly_rate: float
    travel_cost: float
    labor_minutes: int
    labor_cost: float
    material_cost: float
    total_cost: float
    created_at: datetime
    materials: List[MaterialItemResponse]

    class Config:
        from_attributes = True

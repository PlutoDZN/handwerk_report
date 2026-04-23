from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    street = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    job_reports = relationship(
        "JobReport",
        back_populates="customer",
        cascade="all, delete-orphan"
    )


class JobReport(Base):
    __tablename__ = "job_reports"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    work_date = Column(Date, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    description = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    hourly_rate = Column(Float, nullable=False)
    travel_cost = Column(Float, default=0)
    labor_minutes = Column(Integer, nullable=False)
    labor_cost = Column(Float, nullable=False)
    material_cost = Column(Float, nullable=False)
    total_cost = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="job_reports")
    materials = relationship(
        "MaterialItem",
        back_populates="job_report",
        cascade="all, delete-orphan"
    )


class MaterialItem(Base):
    __tablename__ = "material_items"

    id = Column(Integer, primary_key=True, index=True)
    job_report_id = Column(Integer, ForeignKey("job_reports.id"), nullable=False)
    name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)

    job_report = relationship("JobReport", back_populates="materials")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine, Base
from . import models
from .routes import customers, job_reports

app = FastAPI(title="Handwerk Report API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(customers.router)
app.include_router(job_reports.router)


@app.get("/")
def root():
    return {"message": "Handwerk Report API läuft"}

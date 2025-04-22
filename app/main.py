from fastapi import FastAPI
from app.api import fbm

app = FastAPI(title="Geocledian Integration API")

app.include_router(fbm.router, prefix="/api/v1/fbm")

from fastapi import FastAPI
from app.api import fbm
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")

app = FastAPI(title="Geocledian Integration API")

app.include_router(fbm.router, prefix="/api/v1/fbm")

from pydantic import BaseModel, Field
from typing import List, Literal
from datetime import date

class Geometry(BaseModel):
    type: Literal["Polygon"]
    coordinates: List[List[List[float]]]

class FBMUpload(BaseModel):
    submission_id: str
    field_id: str
    geometry: Geometry
    crop_type: str
    region: str
    expected_pick_date: date

class FBMStatusResponse(BaseModel):
    submission_id: str
    field_id: str
    validation: dict
    flag: str

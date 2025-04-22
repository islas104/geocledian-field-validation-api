from fastapi import APIRouter, Depends, HTTPException, status, Header
from app.models.fbm_model import FBMUpload, FBMStatusResponse
from app.services.geocledian_client import save_and_trigger_validation, get_status

API_KEY = "your-secure-api-key"  # Replace with real secret

router = APIRouter()

def verify_api_key(authorization: str = Header(...)):
    try:
        scheme, key = authorization.split()
        if scheme.lower() != "bearer" or key != API_KEY:
            raise ValueError()
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or missing API key.")

@router.post("/upload", response_model=FBMStatusResponse, status_code=status.HTTP_201_CREATED)
async def upload_fbm(data: FBMUpload, _: None = Depends(verify_api_key)):
    result = save_and_trigger_validation(data)
    return result

@router.get("/status/{submission_id}", response_model=FBMStatusResponse)
async def check_status(submission_id: str, _: None = Depends(verify_api_key)):
    result = get_status(submission_id)
    if not result:
        raise HTTPException(status_code=404, detail="Submission ID not found.")
    return result

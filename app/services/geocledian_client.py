from app.models.fbm_model import FBMUpload

# In-memory storage for demo purposes
DB = {}

def save_and_trigger_validation(data: FBMUpload) -> dict:
    validation_result = {
        "luh": True,
        "crop_check": False,
        "net_area": True
    }

    overall_flag = "review" if any(validation_result.values()) else "clear"

    payload = {
        "submission_id": data.submission_id,
        "field_id": data.field_id,
        "validation": validation_result,
        "flag": overall_flag
    }

    DB[data.submission_id] = payload
    return payload

def get_status(submission_id: str):
    return DB.get(submission_id)

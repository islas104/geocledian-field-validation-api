# Geocledian Field Validation API

This FastAPI service is designed to receive and process Field Boundary Mapping (FBM) data for integration with Geocledian's validation workflows. It includes endpoints to submit field data and retrieve validation results using a simple rule-based system, protected by an API key.

---

## 🚀 Features

- `POST /api/v1/fbm/upload` – Accept FBM submissions with geometry and metadata  
- `GET /api/v1/fbm/status/{submission_id}` – Check the validation status of a specific field  
- 🔐 Secured via Bearer token authentication (API key required)  
- ⚙️ Lightweight, no database required (uses in-memory store for quick testing)  
- 📄 Auto-generated Swagger docs at `/docs`

---

## 📦 Requirements

- Python 3.10+
- `pip install -r requirements.txt`

---

## 🛠️ Installation

```bash
git clone https://github.com/islas104/geocledian-field-validation-api.git
cd geocledian-field-validation-api

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🔐 Authentication

All endpoints require an API key to be passed via the Authorization header:

- will be shared with you privately 

## Endpoints

POST /api/v1/fbm/upload
Submit a field for validation.

Request Body:

{
  "submission_id": "abc123",
  "field_id": "field_001",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[72.1, 23.1], [72.2, 23.1], [72.2, 23.2], [72.1, 23.2], [72.1, 23.1]]]
  },
  "crop_type": "cotton",
  "region": "Gujarat",
  "expected_pick_date": "2025-11-15"
}

Response:

{
  "submission_id": "abc123",
  "field_id": "field_001",
  "validation": {
    "luh": true,
    "crop_check": false,
    "net_area": true
  },
  "flag": "review"
}
GET /api/v1/fbm/status/{submission_id}
Retrieve the validation results for a previously submitted field.

Response:

{
  "submission_id": "abc123",
  "field_id": "field_001",
  "validation": {
    "luh": true,
    "crop_check": false,
    "net_area": true
  },
  "flag": "review"
}

## Endpoints

Swagger UI:
http://localhost:8000/docs


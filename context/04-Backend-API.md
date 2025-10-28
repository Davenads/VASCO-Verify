# Backend API Reference

RESTful API design for the platform.

**Base URL**: `http://localhost:8000/api/v1`

## Authentication

MVP does not require authentication (local deployment).  
Future versions will add JWT-based auth for multi-user deployments.

## Common Response Format

### Success Response
```json
{
  "data": {...},
  "message": "Success",
  "timestamp": "2025-10-27T10:30:00Z"
}
```

### Error Response
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input parameters",
    "details": {...}
  },
  "timestamp": "2025-10-27T10:30:00Z"
}
```

## Endpoints

### Health Check

```
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-10-27T10:30:00Z"
}
```

---

### Plates

#### List Plates
```
GET /plates?skip=0&limit=50&sort_by=date_observed&order=desc
```

**Query Parameters:**
- `skip` (int): Pagination offset
- `limit` (int): Results per page (max 100)
- `sort_by` (str): Sort field
- `order` (str): asc/desc

**Response:**
```json
{
  "data": [
    {
      "id": 1,
      "filename": "poss_i_001.fits",
      "date_observed": "1952-07-19T08:52:00Z",
      "ra_center": 180.5234,
      "dec_center": 45.1234,
      "exposure_time": 3000,
      "filter_type": "E",
      "uploaded_at": "2025-10-27T09:00:00Z"
    }
  ],
  "total": 100,
  "skip": 0,
  "limit": 50
}
```

#### Upload Plate
```
POST /plates/upload
Content-Type: multipart/form-data
```

**Request:**
```
file: <FITS file>
```

**Response:**
```json
{
  "id": 123,
  "filename": "uploaded_plate.fits",
  "size": 1024000,
  "status": "uploaded"
}
```

#### Get Plate Details
```
GET /plates/{id}
```

**Response:**
```json
{
  "id": 1,
  "filename": "poss_i_001.fits",
  "date_observed": "1952-07-19T08:52:00Z",
  "ra_center": 180.5234,
  "dec_center": 45.1234,
  "exposure_time": 3000,
  "filter_type": "E",
  "telescope": "Palomar 48-inch Schmidt",
  "observer": "Unknown",
  "file_path": "/data/plates/poss_i_001.fits",
  "file_size": 1024000,
  "uploaded_at": "2025-10-27T09:00:00Z",
  "detection_count": 15
}
```

#### Get Plate Image Data
```
GET /plates/{id}/image?format=png&size=1024
```

**Query Parameters:**
- `format`: png, jpg, fits (default: png)
- `size`: max dimension in pixels (default: 1024)

**Response:** Image binary data

#### Fetch from DSS
```
POST /plates/{id}/fetch
```

**Request:**
```json
{
  "ra": 180.5234,
  "dec": 45.1234,
  "size": 15.0
}
```

**Response:**
```json
{
  "job_id": "fetch_20251027_001",
  "status": "processing"
}
```

---

### Detections

#### Run Detection
```
POST /detections/run
```

**Request:**
```json
{
  "plate_id": 123,
  "confidence_threshold": 0.7,
  "use_gpu": true,
  "crossmatch_catalogs": ["panstarrs", "gaia"],
  "batch_size": 16
}
```

**Response:**
```json
{
  "job_id": "det_20251027_001",
  "status": "processing",
  "plate_id": 123,
  "started_at": "2025-10-27T10:30:00Z",
  "estimated_completion": "2025-10-27T10:30:45Z"
}
```

#### Get Job Status
```
GET /detections/jobs/{job_id}
```

**Response:**
```json
{
  "job_id": "det_20251027_001",
  "status": "completed",
  "progress": 100,
  "results": {
    "detections_found": 15,
    "processing_time": 2.3
  }
}
```

#### List Detections
```
GET /detections?plate_id=123&min_confidence=0.5&verification_status=pending
```

**Response:**
```json
{
  "data": [
    {
      "id": 456,
      "plate_id": 123,
      "ra": 180.5234,
      "dec": 45.1234,
      "magnitude": 18.5,
      "magnitude_error": 0.1,
      "confidence_score": 0.87,
      "detection_method": "yolov8",
      "catalog_match": false,
      "verification_status": "pending",
      "created_at": "2025-10-27T10:30:45Z"
    }
  ],
  "total": 15
}
```

#### Get Detection Details
```
GET /detections/{id}
```

**Response:**
```json
{
  "id": 456,
  "plate_id": 123,
  "ra": 180.5234,
  "dec": 45.1234,
  "magnitude": 18.5,
  "confidence_score": 0.87,
  "bbox": {
    "x": 512.5,
    "y": 768.2,
    "width": 10.5,
    "height": 11.2
  },
  "psf_fit_quality": 0.92,
  "catalog_match": false,
  "verification_status": "pending",
  "verification_count": 0,
  "created_at": "2025-10-27T10:30:45Z"
}
```

---

### Verifications

#### Submit Verification
```
POST /verifications
```

**Request:**
```json
{
  "detection_id": 456,
  "user_id": "anonymous_abc123",
  "status": "accepted",
  "confidence": 4,
  "notes": "Clear point source, no catalog match",
  "tags": ["high_confidence", "isolated"]
}
```

**Response:**
```json
{
  "id": 789,
  "detection_id": 456,
  "status": "accepted",
  "created_at": "2025-10-27T10:35:00Z"
}
```

#### Get Verifications for Detection
```
GET /verifications/detection/{detection_id}
```

**Response:**
```json
{
  "detection_id": 456,
  "verifications": [
    {
      "id": 789,
      "user_id": "anonymous_abc123",
      "status": "accepted",
      "confidence": 4,
      "notes": "Clear point source",
      "created_at": "2025-10-27T10:35:00Z"
    }
  ],
  "consensus": "accepted",
  "agreement_score": 0.85
}
```

---

### Analysis

#### Chi-Square Test
```
POST /analysis/chi-square
```

**Request:**
```json
{
  "contingency_table": [[58, 252], [3756, 23652]],
  "labels": {
    "rows": ["Nuclear Test Window", "Not Nuclear Test Window"],
    "cols": ["Transient", "No Transient"]
  }
}
```

**Response:**
```json
{
  "chi_square": 6.94,
  "p_value": 0.008,
  "degrees_of_freedom": 1,
  "significant": true
}
```

#### Mann-Whitney U Test
```
POST /analysis/mann-whitney
```

**Request:**
```json
{
  "group1": [1, 2, 3, 5, 8, 13],
  "group2": [0, 0, 1, 0, 2, 0, 1]
}
```

**Response:**
```json
{
  "u_statistic": 431649.5,
  "p_value": 0.007,
  "significant": true
}
```

#### Reproduce Paper Findings
```
POST /analysis/reproduce-paper
```

**Request:**
```json
{
  "dataset": "original",
  "tests": ["chi_square", "mann_whitney", "correlation", "glm"]
}
```

**Response:**
```json
{
  "results": {
    "chi_square": {
      "our_value": 6.94,
      "paper_value": 6.94,
      "match": true
    },
    "mann_whitney": {
      "our_p_value": 0.007,
      "paper_p_value": 0.007,
      "match": true
    }
  },
  "overall_match": true,
  "reproducibility_score": 0.98
}
```

---

### Export

#### Export to CSV
```
POST /export/csv
```

**Request:**
```json
{
  "detection_ids": [456, 457, 458],
  "include_verifications": true,
  "include_plate_info": true
}
```

**Response:** CSV file download

#### Export to JSON
```
POST /export/json
```

**Request:**
```json
{
  "detection_ids": "all",
  "filters": {
    "min_confidence": 0.7,
    "verification_status": "accepted"
  }
}
```

**Response:** JSON file download

---

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `VALIDATION_ERROR` | 400 | Invalid request parameters |
| `NOT_FOUND` | 404 | Resource not found |
| `CONFLICT` | 409 | Resource already exists |
| `PROCESSING_ERROR` | 500 | Error during processing |
| `MODEL_ERROR` | 500 | AI model inference failed |
| `DATABASE_ERROR` | 500 | Database operation failed |

## Rate Limiting

- **Detection runs**: 10 per minute per IP
- **Catalog queries**: 100 per hour per IP
- **File uploads**: 5 per minute per IP

Exceeded rate limit returns:
```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests",
    "retry_after": 60
  }
}
```

---

**Implementation**: See [backend/app/api/v1/](../../backend/app/api/v1/) for route implementations

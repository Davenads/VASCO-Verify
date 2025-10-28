"""API endpoints for transient detection operations."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_detections() -> dict:
    """
    List all detections.

    Returns:
        dict: List of detections
    """
    return {"detections": [], "total": 0, "message": "Detections endpoint - coming soon"}


@router.get("/{detection_id}")
async def get_detection(detection_id: int) -> dict:
    """
    Get a specific detection by ID.

    Args:
        detection_id: The detection ID

    Returns:
        dict: Detection details
    """
    return {
        "id": detection_id,
        "message": "Detection detail endpoint - coming soon"
    }


@router.post("/run")
async def run_detection() -> dict:
    """
    Run AI detection on a plate.

    Returns:
        dict: Detection job result
    """
    return {"message": "Run detection endpoint - coming soon"}

"""API endpoints for FITS plate operations."""

from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()


@router.get("/")
async def list_plates() -> dict:
    """
    List all uploaded FITS plates.

    Returns:
        dict: List of plates with metadata
    """
    return {"plates": [], "total": 0, "message": "Plates endpoint - coming soon"}


@router.get("/{plate_id}")
async def get_plate(plate_id: int) -> dict:
    """
    Get a specific plate by ID.

    Args:
        plate_id: The plate ID

    Returns:
        dict: Plate details
    """
    return {
        "id": plate_id,
        "message": "Plate detail endpoint - coming soon"
    }


@router.post("/upload")
async def upload_plate() -> dict:
    """
    Upload a new FITS plate.

    Returns:
        dict: Upload result
    """
    return {"message": "Upload endpoint - coming soon"}

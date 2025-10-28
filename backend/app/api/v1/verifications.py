"""API endpoints for manual verification operations."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_verifications() -> dict:
    """
    List all verifications.

    Returns:
        dict: List of verifications
    """
    return {"verifications": [], "total": 0, "message": "Verifications endpoint - coming soon"}


@router.post("/")
async def create_verification() -> dict:
    """
    Submit a manual verification.

    Returns:
        dict: Created verification
    """
    return {"message": "Create verification endpoint - coming soon"}

"""API endpoints for statistical analysis operations."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_analysis_options() -> dict:
    """
    Get available analysis options.

    Returns:
        dict: Available analysis methods
    """
    return {
        "available_tests": [
            "chi_square",
            "mann_whitney",
            "spearman",
            "glm"
        ],
        "message": "Analysis endpoint - coming soon"
    }


@router.post("/chi-square")
async def run_chi_square() -> dict:
    """
    Run chi-square test for nuclear testing correlation.

    Returns:
        dict: Chi-square test results
    """
    return {"message": "Chi-square test endpoint - coming soon"}


@router.post("/correlations")
async def run_correlations() -> dict:
    """
    Run correlation analysis.

    Returns:
        dict: Correlation results
    """
    return {"message": "Correlation analysis endpoint - coming soon"}

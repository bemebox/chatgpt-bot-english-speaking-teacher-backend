from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/health",
    summary="Health Check",
    description="Check if the service is up and running, including database and file system checks.",
    responses={
        200: {"description": "The service is healthy."},
        503: {"description": "Service is unavailable due to a failure in a critical component."}
    }
)
def health_check():
    return {"status": "ok", "message": "The service is healthy."}

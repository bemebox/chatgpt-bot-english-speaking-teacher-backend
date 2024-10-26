from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.audio_base64 import AudioBase64Payload
from app.models.response import Response
from app.models.response_error import Error
from app.services.speech_analysis import recognize_audio_from_base64

router = APIRouter()

@router.post(
    "/recognition/",
    summary="Upload an audio file for analysis",
    description="This endpoint accepts an audio file, analyzes the speech, and provides feedback on how to improve spoken English.",
    response_description="The analysis feedback in both text and audio format."
)
async def recognize_audio(payload: AudioBase64Payload):
    try:
        result = recognize_audio_from_base64(payload.file)
        return Response(result)
    except ValueError as e:
        # If a ValueError occurs, return a JSONResponse with the Error structure
        error_instance = Error(
            code=400,
            error="Bad Request",
            message=str(e)
        )
        # Return the error response with a 400 status code
        return JSONResponse(
            status_code=400,
            content=error_instance.model_dump()
        )
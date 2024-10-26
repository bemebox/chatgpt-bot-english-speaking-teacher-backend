from fastapi import APIRouter, HTTPException
from models.audio_base64 import AudioBase64Payload
from services.speech_analysis import recognize_audio_from_base64

router = APIRouter()

@router.post(
    "/recognize-audio/",
    summary="Upload an audio file for analysis",
    description="This endpoint accepts an audio file, analyzes the speech, and provides feedback on how to improve spoken English.",
    response_description="The analysis feedback in both text and audio format."
)
async def recognize_audio(payload: AudioBase64Payload):
    try:
        result = recognize_audio_from_base64(payload.file)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
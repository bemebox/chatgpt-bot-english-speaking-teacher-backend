from pydantic import BaseModel

class Response(BaseModel):
    file: str  # the audio file base64 string
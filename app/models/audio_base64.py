from pydantic import BaseModel

class AudioBase64Payload(BaseModel):
    file: str  # Base64 encoded string

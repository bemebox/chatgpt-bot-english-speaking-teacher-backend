from pydantic import BaseModel

class Error(BaseModel):
    code: int   # the error description 
    error: str  # the error description 
    message: str # the error message 
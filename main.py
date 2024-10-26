from fastapi import FastAPI
from app.routes import health as health_route, speech as speech_route

app = FastAPI(
    title="Speech Improvement API",
    description="An API to improve spoken English based on audio input.",
    version="1.0.0"
)

app.include_router(health_route.router, prefix="/api/speech", tags=["health"])
app.include_router(speech_route.router, prefix="/api/speech", tags=["speech"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

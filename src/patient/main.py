from fastapi import FastAPI

app = FastAPI(
    title="Patient API",
    version="0.1.0"
)

from patient.router.patient_router import patient_router

app.include_router(patient_router)

@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}

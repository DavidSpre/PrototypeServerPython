from contextlib import asynccontextmanager

from fastapi import FastAPI

from patient.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="Patient API",
    version="0.1.0",
    lifespan=lifespan
)

from patient.router.patient_router import patient_router

app.include_router(patient_router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}

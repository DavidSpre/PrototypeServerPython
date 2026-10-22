from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from patient.database.database import get_db
from patient.entity import Patient
from patient.schema.schema import PatientCreate, PatientResponse, PatientUpdate

patient_router = APIRouter(prefix="/patients", tags=["patients"])

################################
# GET Requests
################################
@patient_router.get("", response_model=list[PatientResponse])
def get_patients(
    nachname: str | None = None,
    db: Session = Depends(get_db),
) -> Sequence[Patient]:
    statement = select(Patient).order_by(Patient.id)

    if nachname is not None:
        statement = statement.where(Patient.nachname == nachname)

    return db.scalars(statement).all()

@patient_router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(
    patient_id: int, 
    db: Session = Depends(get_db),
) -> Patient:
    patient = db.get(Patient, patient_id)

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient {patient_id} wurde nicht gefunden",
        )
    
    return patient

################################
# POST Requests
################################
@patient_router.post(
    "",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_patient(
    data: PatientCreate,
    db: Session = Depends(get_db),
) -> Patient:
    patient = Patient(
        vorname=data.vorname,
        nachname=data.nachname,
        id=None,
        adresse=None,
        rechnungen=[],
        erzeugt=None,
        aktualisiert=None,
        version=1,
    )

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient

################################
# PUT Requests
################################
@patient_router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(
    patient_id: int,
    data: PatientCreate,
    db: Session = Depends(get_db),
) -> Patient:
    patient = db.get(Patient, patient_id)

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient {patient_id} wurde nicht gefunden."
        )

    if data.version is not patient.version:
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail=f"Patient {patient_id} hat Version {patient.version}. Sie haben gesendet: {data.version}."
        )
    
    patient.vorname = data.vorname
    patient.nachname = data.nachname
    patient.version = patient.version + 1

    db.commit()
    db.refresh(patient)

    return patient

################################
# PATCH Requests
################################
@patient_router.patch("/{patient_id}", response_model=PatientResponse)
def patch_patient(
    patient_id: int,
    data: PatientUpdate,
    db: Session = Depends(get_db),
) -> Patient:
    patient = db.get(Patient, patient_id)

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient {patient_id} wurde nicht gefunden",
        )

    changes = data.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(patient, field, value)

    db.commit()
    db.refresh(patient)

    return patient

################################
# DELETE Requests
################################
@patient_router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
) -> None:
    patient = db.get(Patient, patient_id)

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient {patient_id} wurde nicht gefunden",
        )

    db.delete(patient)
    db.commit()
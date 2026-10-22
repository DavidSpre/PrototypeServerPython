from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class PatientBase(BaseModel):
    vorname: str
    nachname: str


class PatientCreate(PatientBase):
    vorname: str
    nachname: str
    version: int | None = None


class PatientUpdate(BaseModel):
    vorname: str | None = None
    nachname: str | None = None


class AdresseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    plz: str
    ort: str


class PatientResponse(PatientBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    version: int
    erzeugt: datetime | None = None
    aktualisiert: datetime | None = None
    adresse: AdresseResponse | None = None


class RechnungResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    betrag: Decimal
    waehrung: str

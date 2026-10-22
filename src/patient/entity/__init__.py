"""Modul für persistente Patientendaten."""

from patient.entity.adresse import Adresse
from patient.entity.base import Base
from patient.entity.patient import Patient
from patient.entity.rechnung import Rechnung

__all__ = [
    "Adresse",
    "Base",
    "Patient",
    "Rechnung",
]

from typing import override
lazy from decimal import Decimal

from sqlalchemy import ForeignKey, Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

from patient.entity.base import Base
from patient.entity.patient import Patient


class Rechnung(Base):
    """Entity-Klasse für Rechnung."""

    __tablename__ = "rechnung"

    # https://docs.python.org/3/library/decimal.html
    # Genauigkeit ("precision"): 28
    betrag: Mapped[Decimal]

    waehrung: Mapped[str]

    id: Mapped[int | None] = mapped_column(
        Identity(start=1000),
        primary_key=True,
        nullable=False,
    )

    patient_id: Mapped[int | None] = mapped_column(ForeignKey("patient.id"))
    """ID des zugehörigen Patienten als Fremdschlüssel in der DB-Tabelle."""

    patient: Mapped[Patient | None] = relationship(back_populates=Patient.rechnungen)
    """Das zugehörige transiente Patient-Objekt."""

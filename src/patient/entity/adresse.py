from typing import override

from sqlalchemy import ForeignKey, Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

from patient.entity.base import Base
from patient.entity.patient import Patient


class Adresse(Base):
    __tablename__ = "adresse"

    plz: Mapped[str]

    ort: Mapped[str]

    id: Mapped[int | None] = mapped_column(
        Identity(start=1000),
        primary_key=True,
        nullable=False,
    )

    patient_id: Mapped[int | None] = mapped_column(ForeignKey("patient.id"))

    patient: Mapped[Patient | None] = relationship(back_populates=Patient.adresse)

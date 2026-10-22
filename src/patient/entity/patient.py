from typing import Self, override
lazy from dataclasses import InitVar
lazy from datetime import date, datetime

from loguru import logger
from sqlalchemy import JSON, Identity, func
from sqlalchemy.orm import Mapped, mapped_column, reconstructor, relationship

from patient.entity.base import Base
lazy from patient.entity import Adresse, Rechnung

class Patient(Base):
    __tablename__ = "patient"

    vorname: Mapped[str]

    nachname: Mapped[str]

    id: Mapped[int | None] = mapped_column(
        Identity(start=1000),
        primary_key=True,
    )

    adresse: Mapped[Adresse | None] = relationship(
        back_populates=lambda: Adresse.patient,
        innerjoin=True,
        cascade="save-update, delete",
    )
    """Die in einer 1:1-Beziehung referenzierte Adresse."""

    rechnungen: Mapped[list[Rechnung]] = relationship(
        back_populates=lambda: Rechnung.patient,
        cascade="save-update, delete",
    )
    """Die in einer 1:N-Beziehung referenzierten Rechnungen."""

    erzeugt: Mapped[datetime | None] = mapped_column(
        insert_default=func.now(),
    )
    """Der Zeitstempel für das initiale INSERT in die DB-Tabelle."""

    aktualisiert: Mapped[datetime | None] = mapped_column(
        insert_default=func.now(),
        onupdate=func.now(),
    )
    """Der Zeitstempel vom letzen UPDATE in der DB-Tabelle."""

    # https://docs.sqlalchemy.org/en/20/orm/versioning.html#simple-version-counting
    version: Mapped[int] = mapped_column(nullable=False, default=0)
    """Die Versionsnummer für optimistische Synchronisation."""

    # https://docs.sqlalchemy.org/en/20/orm/versioning.html#simple-version-counting
    __mapper_args__ = {"version_id_col": version}  # ruff: ignore[mutable-class-default]

    def set(self, patient: Self) -> None:
        """Primitive Attributwerte überschreiben, z.B. vor DB-Update.

        :param patient: Patient-Objekt mit den aktuellen Daten
        """
        self.vorname = patient.vorname
        self.nachname = patient.nachname

    @override
    def __eq__(self, other: object) -> bool:
        """Vergleich auf Gleicheit, ohne Joins zu verursachen."""
        # Vergleich der Referenzen: id(self) == id(other)
        if self is other:
            return True
        if not isinstance(other, type(self)):
            return False
        return self.id is not None and self.id == other.id

    def __hash__(self) -> int:
        """Hash-Funktion anhand der ID, ohne Joins zu verursachen."""
        return hash(self.id) if self.id is not None else hash(type(self))

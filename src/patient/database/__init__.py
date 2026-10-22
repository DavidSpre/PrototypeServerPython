from patient.database.database import engine
from patient.entity import (
    Adresse as Adresse,
    Base,
    Patient as Patient,
    Rechnung as Rechnung,
)


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)

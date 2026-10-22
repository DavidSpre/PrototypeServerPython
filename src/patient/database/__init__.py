from patient.database.database import engine
from patient.entity import Adresse, Base, Patient, Rechnung

def create_tables() -> None:
    Base.metadata.create_all(bind=engine)

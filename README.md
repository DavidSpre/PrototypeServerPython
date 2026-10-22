# PrototypeServerPython

Repository for the prototype-server using Python, FastAPI, and PostgreSQL. Part of the elective subject "AI-powered server development" by Prof. Dr. Jürgen Zimmermann at HKA

## Requirements

- 1er oder 2er Team:
  - [ ] Informelle Anmeldung per Email bis Fr. 16.10. 12:00 Uhr: Name(n), Matrikelnummer, Link zum GIT-Repo (public)
- Vorbereitet:
  - [ ] Relationale DB mit PostgreSQL 18 oder 19 als Docker Container (mit 3 Tabellen, Haupttabelle und je eine für die folgenden Beziehungen)
    - [ ] 1:1 und 1:N-Beziehung (z.B. Haupttabelle - Kunde, 1:1 - Email, 1:N - Bestellungen; Kundendaten anlegen und Produktartikel ansehen, ...)
    - [ ] DB-Browser
    - [ ] Leeres Git Repository: *"Commit early, Commit often" -> inkrementelle Entwicklung durch Prompts*
- Infrastruktur: **(teil der Abgabe oder Vorbereitet, wie man will)**
  - [ ] pyproject.toml einschl. Konfiguration uv, ruff, ty/pyrefly/pyright
  - [ ] uv
  - [ ] ruff
  - [ ] ty/pyrefly/pyright
- Appserver:
  - [ ] REST durch FastAPI einschl. Dependency Injection und Pydantic für Response
    - [ ] GET-Requests: Pfad- oder Query-Parameter, auch bedingte GET-Requests
    - [ ] POST-Request mit Validierung durch Pydantic
    - [ ] PUT-Request mit Validierung und Vermeidung von Lost-Updates
  - [ ] DB-Zugriff durch SQLAlchemy
- "Testen": GET und POST
  - [ ] Bruno/Postman/Thunder Client *oder*
  - [ ] pytest (Integrationstests genügen)

## Aufsetzen

- Datenbank wie in der vorgegebenen [Anleitung](./extras/compose/postgres/ReadMe.md) beschrieben aufsetzen
- Datenbank starten per Docker: `docker compose -f ./extras/compose/postgres/compose.yml exec postgres psql --dbname=patient --username=postgres`
  - Password: `p`
- Server starten: `uv run fastapi dev`
- Per Bruno testen: `GET`, `POST`, `PUT`, `PATCH`, `DELETE` Requests an `http://localhost:8000/patients`
- Pyrefly ausführen: `uv run pyrefly check`
- ruff ausführen: `uv run ruff check .`

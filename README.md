# PlantOps API

Industrial Maintenance Management (CMMS) backend API designed to centralize plant equipment tracking, fault reporting, work order assignment, and spare parts inventory.

## Problem Statement

Manufacturing plants frequently rely on spreadsheets, paper logs, or disconnected tools to track machine breakdowns and preventive maintenance. This lack of centralization leads to delayed response times, untracked downtime, lost maintenance history, and stockouts of critical spare parts. **PlantOps API** provides a unified, auditable backend to manage the full maintenance lifecycle.

## Target Users

- **Plant Operators:** Report machine anomalies and breakdown incidents from the shop floor.
- **Maintenance Technicians:** Receive assigned work orders, log repair actions, and record spare parts consumption.
- **Maintenance Planners & Supervisors:** Register industrial assets, prioritize repairs, track equipment health, and audit maintenance KPIs.

## Out of Scope

- **Frontend / UI Application:** This repository strictly provides the RESTful backend API. Web or mobile interfaces are managed separately.
- **Direct PLC / SCADA / IoT Telemetry Ingestion:** Real-time high-frequency sensor streaming is excluded; the API handles operational and transactional maintenance records.
- **ERP / Payroll / Financial Accounting:** Invoicing, purchasing workflows, and human resources payroll remain outside this service boundary.

## Technology Stack

### Current Tooling (Phase 1 - Project Scaffold)

- **Language:** Python 3.14
- **Package & Environment Manager:** [uv](https://docs.astral.sh/uv/)
- **Build Backend:** `uv_build` (src-layout package)
- **Linter & Formatter:** Ruff
- **Static Type Checker:** MyPy (`strict = true`)

### Planned Stack (Upcoming Phases)

- **Web Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Data Validation & Settings:** Pydantic v2 / `pydantic-settings`
- **Database ORM & Migrations:** SQLAlchemy 2.0 + Alembic
- **Testing Suite:** pytest + httpx

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed on your system.
- Python 3.14 (automatically managed via `uv python install 3.14`).

## Local Setup

```bash
git clone https://github.com/AntonioMedina08/plantops-api.git
cd plantops-api
uv sync
```

## Quality Checks & Verification

Run the local verification commands before opening or updating a pull request:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv lock --check
uv run plantops-api
```

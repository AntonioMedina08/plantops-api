# PlantOps API

Backend de gestión de mantenimiento industrial (CMMS). Las plantas registran máquinas,
reportan fallas, asignan órdenes de trabajo y controlan refacciones.

## Stack

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.14 |
| Framework | FastAPI |
| Servidor | Uvicorn |
| Validación | Pydantic v2 |
| Gestor de paquetes | uv |
| Lint / Format | Ruff |
| Type checking | MyPy (strict) |
| Tests | pytest + httpx |

## Requisitos

- [uv](https://docs.astral.sh/uv/) instalado
- Python 3.14 (uv lo instala automáticamente con `uv python install 3.14`)

## Configuración local

```bash
git clone <repo-url> plantops-api
cd plantops-api
uv sync                    # crea .venv e instala todo desde uv.lock
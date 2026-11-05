from dataclasses import dataclass, field
from enum import StrEnum
from typing import Final


class DomainError(Exception):
    """Excepción base para reglas de dominio de PlantOps."""

    pass


class InvalidTransitionError(DomainError):
    """Lanzada cuando se intenta una transición de estado no permitida."""

    pass


class WorkOrderStatus(StrEnum):
    OPEN = "OPEN"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"


# Tabla de transiciones permitidas (Estado actual -> Estados destino)
_ALLOWED_TRANSITIONS: Final[dict[WorkOrderStatus, set[WorkOrderStatus]]] = {
    WorkOrderStatus.OPEN: {WorkOrderStatus.ASSIGNED},
    WorkOrderStatus.ASSIGNED: {WorkOrderStatus.IN_PROGRESS},
    WorkOrderStatus.IN_PROGRESS: {WorkOrderStatus.CLOSED},
    WorkOrderStatus.CLOSED: set(),
}


@dataclass(slots=True)
class WorkOrder:
    machine_id: str
    description: str
    technician_id: str | None = field(default=None, init=False)
    resolution: str | None = field(default=None, init=False)
    _status: WorkOrderStatus = field(default=WorkOrderStatus.OPEN, init=False)

    def __post_init__(self) -> None:
        if not self.machine_id or not self.machine_id.strip():
            raise ValueError("El ID de la máquina no puede estar vacío")
        if not self.description or not self.description.strip():
            raise ValueError("La descripción no puede estar vacía")

    @property
    def status(self) -> WorkOrderStatus:
        return self._status

    def _transition_to(self, new_status: WorkOrderStatus) -> None:
        if new_status not in _ALLOWED_TRANSITIONS[self._status]:
            raise InvalidTransitionError(
                f"Transición inválida de {self._status} a {new_status}"
            )
        self._status = new_status

    """   
    def assign(self, technician_id: str) -> None:
        self._transition_to(WorkOrderStatus.ASSIGNED)
        self.technician_id = technician_id
    """

    def assign(self, technician_id: str) -> None:
        if not technician_id or not technician_id.strip():
            raise ValueError("El ID del técnico no puede estar vacío")
        self._transition_to(WorkOrderStatus.ASSIGNED)
        self.technician_id = technician_id

    def start(self) -> None:
        self._transition_to(WorkOrderStatus.IN_PROGRESS)

    def close(self, resolution: str) -> None:
        if not resolution or not resolution.strip():
            raise ValueError("La resolución no puede estar vacía")
        self._transition_to(WorkOrderStatus.CLOSED)
        self.resolution = resolution

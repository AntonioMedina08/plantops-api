import pytest

from plantops_api.domain.work_order import (
    InvalidTransitionError,
    WorkOrder,
    WorkOrderStatus,
)


def test_full_happy_path_flow() -> None:
    order = WorkOrder(machine_id="M-01", description="Falla de motor")
    assert order.status == WorkOrderStatus.OPEN

    order.assign("TECH-123")
    assert order.status == WorkOrderStatus.ASSIGNED  # type: ignore[comparison-overlap]
    assert order.technician_id == "TECH-123"

    order.start()
    assert order.status == WorkOrderStatus.IN_PROGRESS

    order.close("Motor reemplazado")
    assert order.status == WorkOrderStatus.CLOSED
    assert order.resolution == "Motor reemplazado"


def test_empty_description_raises_error() -> None:
    with pytest.raises(ValueError, match="vacía"):
        WorkOrder(machine_id="M-01", description="   ")


def test_close_with_empty_resolution_raises_error() -> None:
    order = WorkOrder(machine_id="M-01", description="Fuga de aceite")
    order.assign("TECH-123")
    order.start()

    with pytest.raises(ValueError, match="vacía"):
        order.close("   ")


def test_invalid_transition_open_to_in_progress() -> None:
    order = WorkOrder(machine_id="M-01", description="Fuga de aceite")

    with pytest.raises(InvalidTransitionError, match="Transición inválida"):
        order.start()


def test_invalid_transition_closed_to_assigned() -> None:
    order = WorkOrder(machine_id="M-01", description="Fuga de aceite")
    order.assign("TECH-123")
    order.start()
    order.close("Fuga reparada")

    with pytest.raises(InvalidTransitionError, match="Transición inválida"):
        order.assign("TECH-456")


def test_state_unchanged_after_failed_transition() -> None:
    order = WorkOrder(machine_id="M-01", description="Válvula rota")
    assert order.status == WorkOrderStatus.OPEN
    assert order.technician_id is None

    # Intentar asignar sin proporcionar un technician_id válido falla
    # por firma de función, pero si forzamos un error lógico (ej. brincar estado):
    with pytest.raises(InvalidTransitionError):
        order.start()

    # El estado no debe mutar
    assert order.status == WorkOrderStatus.OPEN
    assert order.technician_id is None

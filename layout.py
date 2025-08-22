from ignis import widgets
from clock import clock
from workspaces import client_title, workspaces, niri
from audio import speaker_volume
from power import power_menu
from battery import BatteryStatus

def left(monitor_name: str) -> widgets.Box:
    return widgets.Box(
        child=[clock(),client_title(monitor_name)], spacing=10
    )


def center(monitor_name: str) -> widgets.Box:
    return widgets.Box(
        child=[
            workspaces(monitor_name),
        ],
        spacing=10,
    )


def right() -> widgets.Box:
    return widgets.Box(
        child=[
            speaker_volume(),
            BatteryStatus(),
            power_menu(),
        ],
        spacing=10,
    )

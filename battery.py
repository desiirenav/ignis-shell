from ignis import widgets
from ignis.services.upower import UPowerDevice, UPowerService


upower = UPowerService.get_default()


class BatteryItem(widgets.Box):
    def __init__(self, device: UPowerDevice):
        super().__init__(
            css_classes=["battery-item"],
            setup=lambda self: device.connect("removed", lambda _: self.unparent()),
            child=[
                widgets.Icon(image=device.bind("icon-name")),
                widgets.Label(
                    label=device.bind("percent", lambda v: str(round(v)) + "%")
                ),
            ],
        )


class BatteryStatus(widgets.Box):
    def __init__(self, **kwargs):
        super().__init__(
            css_classes=["battery-status"],
            setup=lambda self: upower.connect(
                "battery-added", lambda _, device: self.append(BatteryItem(device))
            ),
            **kwargs,
        )

        def toggle_visible():            
            self.visible = upower.bind("batteries", lambda v: bool(v))
            toggle_visible()

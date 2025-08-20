from ignis import widgets
from ignis.menu_model import IgnisMenuModel, IgnisMenuItem, IgnisMenuSeparator
from workspaces import niri

def logout() -> None:
    if niri.is_available:
        create_exec_task("niri msg action quit")
    else:
        pass


def power_menu() -> widgets.Button:
    menu = widgets.PopoverMenu(
        model=IgnisMenuModel(
            IgnisMenuItem(
                label="Lock",
                on_activate=lambda x: create_exec_task("swaylock"),
            ),
            IgnisMenuSeparator(),
            IgnisMenuItem(
                label="Suspend",
                on_activate=lambda x: create_exec_task("systemctl suspend"),
            ),
            IgnisMenuItem(
                label="Hibernate",
                on_activate=lambda x: create_exec_task("systemctl hibernate"),
            ),
            IgnisMenuSeparator(),
            IgnisMenuItem(
                label="Reboot",
                on_activate=lambda x: create_exec_task("systemctl reboot"),
            ),
            IgnisMenuItem(
                label="Shutdown",
                on_activate=lambda x: create_exec_task("systemctl poweroff"),
            ),
            IgnisMenuSeparator(),
            IgnisMenuItem(
                label="Logout",
                enabled=niri.is_available,
                on_activate=lambda x: logout(),
            ),
        ),
    )
    return widgets.Button(
        child=widgets.Box(
            child=[widgets.Icon(image="system-shutdown-symbolic", pixel_size=20), menu]
        ),
        on_click=lambda x: menu.popup(),
    )


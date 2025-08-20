import os
import datetime
import asyncio
from ignis.menu_model import IgnisMenuModel, IgnisMenuItem, IgnisMenuSeparator
from ignis import widgets
from ignis import utils
from ignis.css_manager import CssManager, CssInfoPath
from ignis.services.audio import AudioService
from ignis.services.niri import NiriService, NiriWorkspace
from ignis.services.notifications import NotificationService
from ignis.services.mpris import MprisService, MprisPlayer
from work import client_title, workspaces, niri

css_manager = CssManager.get_default()

css_manager.apply_css(
    CssInfoPath(
        name="main",
        compiler_function=lambda path: utils.sass_compile(path=path),
        path=os.path.join(utils.get_current_dir(), "style.scss"),
    )
)


audio = AudioService.get_default()
notifications = NotificationService.get_default()
mpris = MprisService.get_default()


def clock() -> widgets.Label:
    # poll for current time every second
    return widgets.Label(
        css_classes=["clock"],
        label=utils.Poll(
            1_000, lambda self: datetime.datetime.now().strftime("%H:%M")
        ).bind("output"),
    )


def speaker_volume() -> widgets.Box:
    return widgets.Box(
        child=[
            widgets.Icon(
                image=audio.speaker.bind("icon_name"), style="margin-right: 5px;"
            ),
            widgets.Label(
                label=audio.speaker.bind("volume", transform=lambda value: str(value))
            ),
        ]
    )




def speaker_slider() -> widgets.Scale:
    return widgets.Scale(
        min=0,
        max=100,
        step=1,
        value=audio.speaker.bind("volume"),
        on_change=lambda x: audio.speaker.set_volume(x.value),
        css_classes=["volume-slider"],  # we will customize style in style.css
    )


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


def left(monitor_name: str) -> widgets.Box:
    return widgets.Box(
        child=[clock(), client_title(monitor_name)], spacing=10
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
            speaker_slider(),
            power_menu(),
        ],
        spacing=10,
    )


def bar(monitor_id: int = 0) -> widgets.Window:
    monitor_name = utils.get_monitor(monitor_id).get_connector()  # type: ignore
    return widgets.Window(
        namespace=f"ignis_bar_{monitor_id}",
        monitor=monitor_id,
        anchor=["left", "top", "right"],
        exclusivity="exclusive",
        child=widgets.CenterBox(
            css_classes=["bar"],
            start_widget=left(monitor_name),  # type: ignore
            center_widget=center(monitor_name),
            end_widget=right(),
        ),
    )


# this will display bar on all monitors
for i in range(utils.get_n_monitors()):
    bar(i)

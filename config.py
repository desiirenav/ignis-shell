import os
import datetime
import asyncio
from ignis.menu_model import IgnisMenuModel, IgnisMenuItem, IgnisMenuSeparator
from ignis import widgets
from ignis import utils
from ignis.css_manager import CssManager, CssInfoPath
from ignis.services.niri import NiriService, NiriWorkspace
from workspaces import client_title, workspaces, niri
from audio import speaker_volume
from clock import clock
from power import logout, power_menu
from layout import  left, center, right

css_manager = CssManager.get_default()

css_manager.apply_css(
    CssInfoPath(
        name="main",
        compiler_function=lambda path: utils.sass_compile(path=path),
        path=os.path.join(utils.get_current_dir(), "style.scss"),
    )
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

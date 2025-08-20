from ignis import widgets
from ignis.services.niri import NiriService, NiriWorkspace

niri = NiriService.get_default()

def niri_workspace_button(workspace: NiriWorkspace) -> widgets.Button:
    widget = widgets.Button(
        css_classes=["workspace"],
        on_click=lambda x: workspace.switch_to(),
        child=widgets.Label(label=str(workspace.idx)),
    )
    if workspace.is_active:
        widget.add_css_class("active")

    return widget


def workspace_button(workspace) -> widgets.Button:
    if niri.is_available:
        return niri_workspace_button(workspace)
    else:
        return widgets.Button()


def niri_scroll_workspaces(monitor_name: str, direction: str) -> None:
    current = list(
        filter(lambda w: w.is_active and w.output == monitor_name, niri.workspaces)
    )[0].idx
    if direction == "up":
        target = current + 1
        niri.switch_to_workspace(target)
    else:
        target = current - 1
        niri.switch_to_workspace(target)


def scroll_workspaces(direction: str, monitor_name: str = "") -> None:
    if niri.is_available:
        niri_scroll_workspaces(monitor_name, direction)
    else:
        pass


def niri_workspaces(monitor_name: str) -> widgets.EventBox:
    return widgets.EventBox(
        on_scroll_up=lambda x: scroll_workspaces("up", monitor_name),
        on_scroll_down=lambda x: scroll_workspaces("down", monitor_name),
        css_classes=["workspaces"],
        spacing=5,
        child=niri.bind(
            "workspaces",
            transform=lambda value: [
                workspace_button(i) for i in value if i.output == monitor_name
            ],
        ),
    )


def workspaces(monitor_name: str) -> widgets.EventBox:
    if niri.is_available:
        return niri_workspaces(monitor_name)
    else:
        return widgets.EventBox()



def niri_client_title(monitor_name) -> widgets.Label:
    return widgets.Label(
        ellipsize="end",
        max_width_chars=40,
        visible=niri.bind("active_output", lambda output: output == monitor_name),
        label=niri.active_window.bind("title"),
    )


def client_title(monitor_name: str) -> widgets.Label:
    if niri.is_available:
        return niri_client_title(monitor_name)
    else:
        return widgets.Label()


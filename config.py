from ignis import widgets
from widgets import clock

class Bar(widgets.Window):
    def _init_(self, monitor: int):
        super().__init__(
            name="bar",
            layer="top",
            anchor= ["left", "top", "right"],
            margin="5px 10px -2px 5px",
            exclusivity="auto",
            visible=False,
            child=widgets.CenterBox(
                 end_widget=widgets.Box(
                     child=[clock()]
                 ),
            ),
        )


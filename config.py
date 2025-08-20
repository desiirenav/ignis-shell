from ignis import widgets
from bar import bar 

def bar() -> widgets.Window:
    return widgets.Window(
            anchor=["left", "top", "right"],
            exclusivity="exclusive",
            child=widgets.CenterBox(
                center_widget=center(),
            ),
    ),

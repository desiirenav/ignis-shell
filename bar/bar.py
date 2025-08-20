from ignis import widgets
from widgets. import time

def center() -> widgets.Box:
    return widgets.Box(
        child=[
            clock()
        ],
        spacing=10,
    )

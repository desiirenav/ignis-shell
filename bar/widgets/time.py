from ignis import widgets

def clock() -> widgets.Label:
    # poll for current time every second
    return widgets.Label(
        css_classes=["clock"],
        label=utils.Poll(
            1_000, lambda self: datetime.datetime.now().strftime("%H:%M")
        ).bind("output"),
    )

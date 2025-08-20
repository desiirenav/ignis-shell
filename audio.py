from ignis import widgets
from ignis.services.audio import AudioService
from ignis.services.mpris import MprisService, MprisPlayer

audio = AudioService.get_default()



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

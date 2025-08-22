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




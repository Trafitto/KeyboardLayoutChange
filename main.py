from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

import subprocess


class KeyboardLayoutChange(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_query().strip()
        if query == extension.preferences['kus']:
            subprocess.Popen(['setxkbmap', 'us', '-variant', 'alt-intl'])
        if query == extension.preferences['kusa']:
            subprocess.Popen(['setxkbmap', 'us'])
        elif query == extension.preferences['kit']:
            subprocess.Popen(['setxkbmap', 'it'])
        elif query == extension.preferences['kes']:
            subprocess.Popen(['setxkbmap', 'es'])
        elif query == extension.preferences['kfr']:
            subprocess.Popen(['setxkbmap', 'fr'])
        elif query == extension.preferences['kpl']:
            subprocess.Popen(['setxkbmap', 'pl'])
        elif query == extension.preferences['kde']:
            subprocess.Popen(['setxkbmap', 'de'])
        elif query == extension.preferences['kdha']:
            subprocess.Popen(['setxkbmap', 'us', '-variant', 'colemak_dh'])
        elif query == extension.preferences['kdhi']:
            subprocess.Popen(['setxkbmap', 'us', '-variant', 'colemak_dh_iso'])
        elif query == extension.preferences['ja']:
            subprocess.Popen(['setxkbmap', 'ja'])
        elif query == extension.preferences['he']:
            subprocess.Popen(['setxkbmap', 'he'])
        elif query == extension.preferences['ru']:
            subprocess.Popen(['setxkbmap', 'ru'])
        elif query == extension.preferences['sv']:
            subprocess.Popen(['setxkbmap', 'sv'])
        elif query == extension.preferences['sl']:
            subprocess.Popen(['setxkbmap', 'sl'])
        elif query == extension.preferences['ch']:
            subprocess.Popen(['setxkbmap', 'ch'])
        elif query == extension.preferences['sq']:
            subprocess.Popen(['setxkbmap', 'sq'])
        elif query == extension.preferences['be']:
            subprocess.Popen(['setxkbmap', 'be'])
        elif query == extension.preferences['da']:
            subprocess.Popen(['setxkbmap', 'da'])
        elif query == extension.preferences['nl']:
            subprocess.Popen(['setxkbmap', 'nl'])
        elif query == extension.preferences['kbr']:
            subprocess.Popen(['setxkbmap', 'br', '-model', 'abnt2',])
        return HideWindowAction()


if __name__ == '__main__':
    KeyboardLayoutChange().run()

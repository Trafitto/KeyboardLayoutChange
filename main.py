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
        return HideWindowAction()
        

if __name__ == '__main__':
    KeyboardLayoutChange().run()
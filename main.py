from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

import subprocess
import logging
logger = logging.getLogger(__name__)

# setxkbmap us -variant alt-intl
# subprocess.Popen(['setxkbmap', 'us' , '-variant', 'alt-intl'])



class KeyboardLayoutChange(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_query().strip()
        if query == extension.preferences['kus']:
            subprocess.Popen(['setxkbmap', 'us' , '-variant', 'alt-intl'])
        elif query == extension.preferences['kit']:
            subprocess.Popen(['setxkbmap', 'it'])
        return HideWindowAction()
        

if __name__ == '__main__':
    KeyboardLayoutChange().run()
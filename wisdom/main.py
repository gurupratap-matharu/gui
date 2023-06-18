import logging

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from quotes import get_quote

kivy.require("2.2.0")

logger = logging.getLogger(__name__)


class MyRootWidget(BoxLayout):
    def on_button_press(self):
        """
        Get a new quote and display it on the UI
        """

        logger.info("button pressed...")

        quote = get_quote()
        self.ids.quote.text = f"[color=ca921a]{quote}[/color]"


class WisdomApp(App):
    def build(self):
        root = MyRootWidget()
        return root


if __name__ == "__main__":
    app = WisdomApp()
    app.run()

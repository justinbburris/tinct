from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty

from hue import Hue
import settings

class LightGroupPanel(BoxLayout):
    hue_bridge = ObjectProperty(None)
    light_groups = ListProperty([])

    def on_hue_bridge(self, instance, pos):
        self.light_groups = [group['name'] for group in self.hue_bridge.groups()]

class Tinct(Widget):

    hue_bridge = ObjectProperty(None)

    def setup_hue_bridge(self):
        self.hue_bridge = Hue(settings.HUE_USERNAME, settings.HUE_BRIDGE_IP)

class TinctApp(App):

    def build(self):
        tinct = Tinct()
        tinct.setup_hue_bridge()
        return tinct

if __name__ == '__main__':
    TinctApp().run()

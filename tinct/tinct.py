from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty

from hue import Hue
import settings

class GroupControlPanel(BoxLayout):
    hue_bridge = ObjectProperty(None)
    selected_group = ObjectProperty(None)
    lights = ListProperty([])

    def on_selected_group(self, instance, pos):
        group_id = int(self.selected_group['id'])
        group = self.hue_bridge.groups(group_id)
        lights = [self.hue_bridge.lights(int(light_id)) for light_id in group['lights']]
        self.lights = [light['name'] for light in lights]

class LightGroupPanel(BoxLayout):
    hue_bridge = ObjectProperty(None)
    selected_group = ObjectProperty(None)
    light_groups = ListProperty([])

    def on_hue_bridge(self, instance, pos):
        groups = self.hue_bridge.groups()

        self.light_groups = [group['name'] for group in groups]
        self.selected_group = groups[0]

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

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty

from hue import Hue
import settings

class LightButton(Button):
    BULB_OFF='assets/images/bulb_off.png'
    BULB_ON='assets/images/bulb_on.png'

    light = ObjectProperty(None)
    image_src = StringProperty(BULB_OFF)

    def __init__(self, **kwargs):
        self.light=kwargs['light']

        if self.light['state']['on']:
            self.image_src = self.BULB_ON

        super(LightButton, self).__init__(**kwargs)

class GroupLights(StackLayout):

    hue_bridge = ObjectProperty(None)
    selected_group = ObjectProperty(None)

    def on_selected_group(self, instance, pos):
        group_id = int(self.selected_group['id'])
        group = self.hue_bridge.groups(group_id)
        lights = [self.hue_bridge.lights(int(light_id)) for light_id in group['lights']]

        for light in lights:
            self.add_widget(LightButton(light=light))

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

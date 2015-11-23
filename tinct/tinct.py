from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty

from hue import Hue
import settings

class GroupOnToggleButton(Button):

    STATE_ON = 'Turn Off'
    STATE_OFF = 'Turn On'

    on_state = StringProperty(STATE_ON)

    def on_press(self):
        pass

class LightButton(Button):
    BULB_OFF='assets/images/bulb_off.png'
    BULB_ON='assets/images/bulb_on.png'

    light = ObjectProperty(None)
    image_src = StringProperty(BULB_OFF)

    def __init__(self, **kwargs):
        self.hue_bridge = kwargs['hue_bridge']
        self.light_id = kwargs['light_id']
        self.light = kwargs['light']

        self.update_image_src()

        super(LightButton, self).__init__(**kwargs)

    def update_image_src(self):
        if self.light['state']['on']:
            self.image_src = self.BULB_ON
        else:
            self.image_src = self.BULB_OFF

    def on_press(self):
        new_state = not self.light['state']['on']

        self.hue_bridge.light_set_on(self.light_id, new_state)
        self.light = self.hue_bridge.lights(self.light_id)

    def on_light(self, instance, pos):
        self.update_image_src()

class GroupLights(StackLayout):

    hue_bridge = ObjectProperty(None)
    selected_group = ObjectProperty(None)

    def on_selected_group(self, instance, pos):
        group_id = int(self.selected_group['id'])
        group = self.hue_bridge.groups(group_id)
        for light_id in group['lights']:
            id = int(light_id)
            light = self.hue_bridge.lights(id)
            self.add_widget(
                    LightButton(light_id= id, hue_bridge=self.hue_bridge, light=light)
                    )

class GroupPanel(RelativeLayout):

    pass

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

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
import settings


class LightGroupList(BoxLayout):
    from hue import Hue
    h = Hue(settings.HUE_USERNAME, settings.HUE_BRIDGE_IP)
    light_groups = ListProperty([group['name'] for group in h.groups()['resource']])

class Tinct(Widget):
    pass


class TinctApp(App):
    def build(self):
        return Tinct()

if __name__ == '__main__':
    TinctApp().run()

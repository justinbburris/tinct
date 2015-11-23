import subprocess
import time

from hue import Hue

from nose.tools import assert_equal

def setup_module(self):
    self.honcho_process = subprocess.Popen(['honcho', 'start'], cwd='..')
    time.sleep(1) # need to wait for huesimulator to finish spawning

def teardown_module(self):
    self.honcho_process.terminate()

class TestHue(object):

    def setup(self):
        self.hue = Hue('newdeveloper', 'localhost:8080')

    def test_init(self):
        assert_equal(self.hue.bridge_ip, 'localhost:8080')
        assert_equal(self.hue.user_id, 'newdeveloper')

    def test_groups(self):
        groups = [{u'name': u'Group 1', 'id': 1}]
        assert_equal(self.hue.groups(), groups)

    def test_single_group(self):
        group = {u'action': {u'on': True}, u'lights': [u'1', u'2'], u'name': u'Group 1'}
        assert_equal(self.hue.groups(1), group)

    def test_turn_on_group(self):
        result = {'resource': [{u'success': {u'/groups/1/action/on': True}}]}
        assert_equal(self.hue.group_set_on(1, True), result)

    def test_turn_off_group(self):
        result = {'resource': [{u'success': {u'/groups/1/action/on': False}}]}
        assert_equal(self.hue.group_set_on(1, False), result)

    def test_single_light(self):
        light = {
                u'name': u'Hue Lamp 1',
                u'swversion': u'65003148',
                u'pointsymbol': {
                    u'1': u'none',
                    u'3': u'none',
                    u'2': u'none',
                    u'5': u'none',
                    u'4': u'none',
                    u'7': u'none',
                    u'6': u'none',
                    u'8': u'none'
                },
                u'state': {
                    u'on': True,
                    u'hue': 0,
                    u'colormode': u'hs',
                    u'effect': u'none',
                    u'alert':
                    u'none',
                    u'xy': [0, 0],
                    u'reachable': True,
                    u'bri': 0,
                    u'sat': 0,
                    u'ct': 0
                },
                u'type': u'Extended color light',
                u'modelid': u'LCT001'
            }
        assert_equal(self.hue.lights(1), light)

    def test_turn_on_light(self):
        result = {'resource': [{u'success': {u'/lights/1/state/on': True}}]}
        assert_equal(self.hue.light_set_on(1, True), result)

    def test_turn_off_light(self):
        result = {'resource': [{u'success': {u'/lights/2/state/on': False}}]}
        assert_equal(self.hue.light_set_on(2, False), result)

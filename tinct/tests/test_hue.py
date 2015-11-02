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
        groups = {'resource': [{u'name': u'Group 1', 'id': 1}]}
        assert_equal(self.hue.groups(), groups)

    def test_single_group(self):
        group = {'resource': {u'action': {u'on': True, u'hue': 33536, u'colormode': u'xy', u'effect': u'none', u'xy': [0.346, 0.3568], u'bri': 254, u'sat': 144, u'ct': 201}, u'lights': [u'1', u'2'], u'name': u'Group 1'}}
        assert_equal(self.hue.groups(1), group)

    def test_turn_on_group(self):
        result = {'resource': [{u'success': {u'/groups/1/action/on': True}}]}
        assert_equal(self.hue.group_set_on(1, True), result)

    def test_turn_off_group(self):
        result = {'resource': [{u'success': {u'/groups/1/action/on': False}}]}
        assert_equal(self.hue.group_set_on(1, False), result)

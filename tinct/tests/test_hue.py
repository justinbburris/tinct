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

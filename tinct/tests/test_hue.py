from hue import Hue

from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

class TestHue(object):
    def test_init(self):
        a = Hue('user_id')
        assert_equal(a.userid, 'user_id')

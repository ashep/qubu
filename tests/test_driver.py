"""Driver Tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import qubu


class TestDriver:
    """Test driver() API function
    """

    def test_get_default_driver(self):
        assert qubu.driver() == qubu.drivers.mongodb

    def test_set_driver(self):
        assert qubu.driver(qubu.drivers.mongodb) == qubu.drivers.mongodb

"""Database Query Builder
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from qubu import contract
from ._expression import MongoDBExpression


class Near(MongoDBExpression, contract.Near):
    """Search for geospatial objects in proximity to a point
    """

    def __init__(self, field: str, **kwargs):
        super().__init__(field, **kwargs)

        self._lng = kwargs.get('lng', 0)
        self._lat = kwargs.get('lat', 0)
        self._min_distance = kwargs.get('min_distance')
        self._max_distance = kwargs.get('max_distance')

    def compile(self) -> dict:
        """Compile the expression
        """
        r = {
            self._field: {
                self.name: {
                    '$geometry': {
                        'type': 'Point',
                        'coordinates': [self._lng, self._lat],
                    }
                }
            }
        }

        if self._min_distance:
            r[self._field][self.name]['$minDistance'] = self._min_distance

        if self._max_distance:
            r[self._field][self.name]['$maxDistance'] = self._max_distance

        return r


class NearSphere(Near, contract.NearSphere):
    """Search for geospatial objects in proximity to a point on a sphere
    """
    pass

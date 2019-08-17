"""QuBu Geospatial Expressions Contracts
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from abc import ABC
from ._expression import FieldExpression


class GeospatialExpression(FieldExpression, ABC):
    """Base Geospatial Expression
    """

    def __init__(self, field: str, **kwargs):
        super().__init__(field, None)


class Near(GeospatialExpression):
    """Search for geospatial objects in proximity to a point
    """
    pass


class NearSphere(GeospatialExpression):
    """Search for geospatial objects in proximity to a point on a sphere
    """
    pass

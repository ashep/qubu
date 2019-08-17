"""QuBu Comparison Expressions Contracts
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from abc import ABC
from ._expression import FieldExpression


class Eq(FieldExpression, ABC):
    """Matches values that are equal to a specified value
    """
    pass


class Gt(FieldExpression, ABC):
    """Matches values that are greater than a specified value
    """
    pass


class Gte(FieldExpression, ABC):
    """Matches values that are greater than or equal to a specified value
    """
    pass


class In(FieldExpression, ABC):
    """Matches any of the values specified in an array
    """
    pass


class Lt(FieldExpression, ABC):
    """Matches values that are less than a specified value
    """
    pass


class Lte(FieldExpression, ABC):
    """Matches values that are less than or equal to a specified value
    """
    pass


class Ne(FieldExpression, ABC):
    """Matches all values that are not equal to a specified value
    """
    pass


class Nin(FieldExpression, ABC):
    """Matches none of the values specified in an array
    """
    pass

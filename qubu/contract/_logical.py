"""QuBu Logical Expressions Contracts
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

__all__ = ['And', 'Or', 'Not', 'Nor']

from abc import ABC
from ._expression import FieldOperatorExpression, UnionExpression


class And(UnionExpression, ABC):
    """Joins expressions with the AND logical operator
    """
    pass


class Or(UnionExpression, ABC):
    """Joins expressions with the OR logical operator
    """
    pass


class Not(FieldOperatorExpression, ABC):
    """Inverts the effect of an expression
    """
    pass


class Nor(UnionExpression, ABC):
    """Joins expressions with the NOR logical operator
    """
    pass

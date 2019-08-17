"""QuBu Logical Operators
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from ._expression import FieldOperatorExpression, UnionExpression


class And(UnionExpression):
    """Join query clauses with a logical AND

    https://docs.mongodb.com/manual/reference/operator/query/and/
    """
    pass


class Or(UnionExpression):
    """Joins query clauses with a logical OR

    https://docs.mongodb.com/manual/reference/operator/query/or/
    """
    pass


class Nor(UnionExpression):
    pass


class Not(FieldOperatorExpression):
    """Inverts the effect of a query expression

    https://docs.mongodb.com/manual/reference/operator/query/not/
    """
    pass

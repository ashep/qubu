"""QuBu Comparison Expressions
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from ._expression import FieldExpression


class Eq(FieldExpression):
    """Matches values that are equal to a specified value

    https://docs.mongodb.com/manual/reference/operator/query/eq/
    """
    pass


class Gt(FieldExpression):
    """Matches values that are greater than a specified value

    https://docs.mongodb.com/manual/reference/operator/query/gt/
    """
    pass


class Gte(FieldExpression):
    """Matches values that are greater than or equal to a specified value

    https://docs.mongodb.com/manual/reference/operator/query/gte/
    """
    pass


class In(FieldExpression):
    """Matches any of the values specified in an array

    https://docs.mongodb.com/manual/reference/operator/query/in/
    """
    pass


class Lt(FieldExpression):
    """Matches values that are less than a specified value

    https://docs.mongodb.com/manual/reference/operator/query/lt/
    """
    pass


class Lte(FieldExpression):
    """Matches values that are less than or equal to a specified value

    https://docs.mongodb.com/manual/reference/operator/query/lte/
    """
    pass


class Ne(FieldExpression):
    """Matches all values that are not equal to a specified value

    https://docs.mongodb.com/manual/reference/operator/query/ne/
    """
    pass


class Nin(FieldExpression):
    """Matches none of the values specified in an array

    https://docs.mongodb.com/manual/reference/operator/query/nin/
    """
    pass

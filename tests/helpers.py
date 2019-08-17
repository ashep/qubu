"""Test Helpers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import random, string
import qubu

DRIVERS = (qubu.drivers.mongodb,)
UNION_EXPRS = ('And', 'Or', 'Nor')
FIELD_OPERATOR_EXPRS = ('Not',)
COMPARISON_EXPRS = ('Eq', 'Gt', 'Gte', 'In', 'Lt', 'Lte', 'Ne', 'Nin')
LOGIGAL_EXPRS = ('And', 'Or', 'Not', 'Nor')
EVALUATION_EXPRS = ('Text', 'Regex')


def random_str(length: int = 8):
    """Generate a random string of fixed length
    """
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def random_comparison_expression(f_name, arg) -> qubu.contract.FieldExpression:
    return getattr(qubu, random.choice(COMPARISON_EXPRS))(f_name, arg)

"""QuBu Evaluation Expression Contracts
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from abc import ABC
from ._expression import Expression, FieldExpression


class EvaluationExpression(Expression, ABC):
    """Evaluation Expression
    """
    pass


class Text(EvaluationExpression, ABC):
    """Text Search Expression
    """

    def __init__(self, **kwargs):
        """Init
        """
        super().__init__()


class Regex(EvaluationExpression, FieldExpression, ABC):
    """Pattern Matching Expression
    """

    def __init__(self, field: str, **kwargs):
        """Init
        """
        super().__init__(field, None)

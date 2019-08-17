"""QuBu MongoВИ Ифыу Expressions
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Any, Dict
from abc import ABC
from dicmer import dict_merge
from qubu import contract


class MongoDBExpression(contract.Expression, ABC):
    """Base Expression
    """

    @property
    def name(self) -> str:
        """Get operator's name
        """
        return '$' + self.__class__.__name__[:1].lower() + self.__class__.__name__[1:]


class FieldExpression(MongoDBExpression, contract.FieldExpression, ABC):
    """Field Expression
    """

    def compile(self) -> Dict[str, Dict]:
        """Compile the expression
        """
        return {self._field: {self.name: self._arg}}


class FieldOperatorExpression(MongoDBExpression, contract.FieldOperatorExpression, ABC):
    """Field Operator Expression
    """

    def compile(self) -> Dict[str, Any]:
        """Compile the expression
        """
        if isinstance(self._arg, FieldExpression):
            return {self._arg.field: {self.name: self._arg.compile()[self._arg.field]}}


class UnionExpression(MongoDBExpression, contract.UnionExpression, ABC):
    """Union Expression
    """

    def remove(self, field: str, _root: contract.Expression = None):
        """Remove all FieldOperators of particular field
        """
        if _root is None:
            _root = self

        ops_to_del = []
        for i, op in enumerate(_root):
            if isinstance(op, FieldExpression) and op.field == field:
                ops_to_del.append(i)

        for i in ops_to_del:
            del _root[i]

        return self

    def compile(self) -> Any:
        """Compile the expression
        """
        r = {}

        for expr in self:
            r = dict_merge(r, expr.compile())

        r = {self.name: [expr.compile() for expr in self if expr]}

        return r if r[self.name] else {}

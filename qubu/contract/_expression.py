"""QuBu Expression Contracts
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

__all__ = ['Expression', 'FieldOperatorExpression', 'FieldExpression', 'UnionExpression']

from typing import Any, Iterator, List
from abc import ABC, abstractmethod


class Expression(ABC):
    """Base Expression
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Get name of the expression
        """
        pass   # pragma: no cover

    @abstractmethod
    def compile(self) -> Any:
        """Compile the expression
        """
        pass   # pragma: no cover

    def __str__(self) -> str:
        """__str__()
        """
        return str(self.compile())

    def __eq__(self, other) -> bool:
        """__eq__()
        """
        return self.compile() == other.compile()


class FieldExpression(Expression, ABC):
    """Field expression
    """

    @property
    def field(self) -> str:
        """Get field's name
        """
        return self._field

    def __init__(self, field: str, arg: Any):
        """Init
        """
        self._field = field
        self._arg = arg


class FieldOperatorExpression(Expression, ABC):
    """Field operator expression
    """

    def __init__(self, arg: FieldExpression):
        """Init
        """
        if not isinstance(arg, FieldExpression):
            raise TypeError(f'Instance of {FieldExpression} expected, not ')

        self._arg = arg


class UnionExpression(Expression, ABC):
    """Union of expressions
    """

    def __init__(self, *children):
        """Init
        """
        self._children = []  # type: List[Expression]

        for c in children:
            self.append(c)

    def __len__(self) -> int:
        """__len__()
        """
        return len(self._children)

    def __iter__(self):
        """__iter__()

        :rtype: Iterator[UnionExpression]
        """
        return iter(self._children)

    def __getitem__(self, key: int):
        """__getitem__()

        :rtype: UnionExpression
        """
        return self._children[key]

    def __delitem__(self, key: int):
        """__delitem__()
        """
        del self._children[key]

    def __contains__(self, item) -> bool:
        """__contains__()
        """
        return item in self._children

    def append(self, expr):
        """Append an expression

        :type expr: Union[FieldExpression, UnionExpression]
        :rtype: UnionExpression
        """
        if not isinstance(expr, Expression):
            raise TypeError(f'Instance of {Expression} expected, not {type(expr)}')

        self._children.append(expr)

        return self

    def remove(self, field: str):
        """Remove FieldExpressions for particular field
        """
        pass  # pragma: no cover

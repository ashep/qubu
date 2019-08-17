"""QuBu API
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

__all__ = [
    'driver',
    'And', 'Or', 'Not', 'Nor',
    'Eq', 'Gt', 'Gte', 'In', 'Lt', 'Lte', 'Ne', 'Nin',
    'Text', 'Regex',
    'Near', 'NearSphere',
]

from typing import Any
from . import contract

_driver = None


def driver(driver=None):
    """Get or set current driver
    """
    global _driver

    if driver is None:
        if _driver is None:
            from .drivers import mongodb
            _driver = mongodb
    else:
        _driver = driver

    return _driver


def And(*children) -> contract.And:
    return driver().And(*children)


def Or(*children) -> contract.Or:
    return driver().Or(*children)


def Not(arg: contract.FieldExpression) -> contract.Not:
    return driver().Not(arg)


def Nor(*children) -> contract.Nor:
    return driver().Nor(*children)


def Eq(field: str, arg: Any) -> contract.Eq:
    return driver().Eq(field, arg)


def Gt(field: str, arg: Any) -> contract.Gt:
    return driver().Gt(field, arg)


def Gte(field: str, arg: Any) -> contract.Gte:
    return driver().Gte(field, arg)


def In(field: str, arg: Any) -> contract.In:
    return driver().In(field, arg)


def Lt(field: str, arg: Any) -> contract.Lt:
    return driver().Lt(field, arg)


def Lte(field: str, arg: Any) -> contract.Lte:
    return driver().Lte(field, arg)


def Ne(field: str, arg: Any) -> contract.Ne:
    return driver().Ne(field, arg)


def Nin(field: str, arg: Any) -> contract.Nin:
    return driver().Nin(field, arg)


def Text(**kwargs) -> contract.Text:
    return driver().Text(**kwargs)


def Regex(field: str, **kwargs) -> contract.Regex:
    return driver().Regex(field, **kwargs)


def Near(field: str, **kwargs) -> contract.Near:
    return driver().Near(field, **kwargs)


def NearSphere(field: str, **kwargs) -> contract.NearSphere:
    return driver().NearSphere(field, **kwargs)

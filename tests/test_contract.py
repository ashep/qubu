"""Contract Tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import random, pytest, qubu
from .helpers import DRIVERS, COMPARISON_EXPRS, UNION_EXPRS, EVALUATION_EXPRS, random_str, random_comparison_expression


class TestContract:
    def test_field_operator_expression_init(self):
        for driver in DRIVERS:
            qubu.driver(driver)

            for bad_arg in [1, '1', 1.0, None, False]:
                with pytest.raises(TypeError):
                    qubu.Not(bad_arg)

    def test_union_expressions(self):
        for driver in DRIVERS:
            qubu.driver(driver)
            for expr_method in UNION_EXPRS:
                children = []
                for n in range(random.randrange(1, len(COMPARISON_EXPRS) + 1)):
                    children.append(random_comparison_expression(random_str(), random_str()))
                expr_obj = getattr(qubu, expr_method)(*children)  # type: qubu.contract.UnionExpression

                # Test __len__()
                assert len(expr_obj) == len(children)

                # Test __getitem__() and __contains__()
                for n in range(len(expr_obj)):
                    assert expr_obj[n] == children[n]
                    assert children[n] in expr_obj

                # Test __delitem()__
                for n in range(len(expr_obj)):
                    del expr_obj[0]

                # Test remove()
                assert len(expr_obj) == 0
                f_name = random_str()
                expr_obj.append(random_comparison_expression(f_name, random_str()))
                assert len(expr_obj) == 1
                expr_obj.remove(f_name)
                assert len(expr_obj) == 0

                # Test invalid child append
                with pytest.raises(TypeError):
                    for o in (1, 0.1, False, None, 'str'):
                        expr_obj.append(o)

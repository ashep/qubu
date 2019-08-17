"""MongoDB Tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import random, pytest, qubu
from qubu.drivers.mongodb import SUPPORTED_LANGS
from .helpers import COMPARISON_EXPRS, LOGIGAL_EXPRS, random_str, random_comparison_expression


class TestMongodb:
    """Test MongoDB
    """

    @classmethod
    def setup_class(cls):
        qubu.driver(qubu.drivers.mongodb)

    def test_comparison_expressions(self):
        for expr_method in COMPARISON_EXPRS:
            f_name = random_str()
            arg = random_str()
            expr_obj_1 = getattr(qubu, expr_method)(f_name, arg)
            expr_obj_2 = getattr(qubu, expr_method)(f_name, arg)
            expected_compiled = {f_name: {f'${expr_method.lower()}': arg}}

            assert expr_obj_1 == expr_obj_2
            assert expr_obj_1.compile() == expected_compiled
            assert str(expr_obj_1) == str(expected_compiled)

    def test_logical_expressions(self):
        # Test all logical expressions except 'Not'
        for expr in LOGIGAL_EXPRS:
            if expr == 'Not':
                continue

            children = []
            for n in range(random.randrange(1, len(COMPARISON_EXPRS) + 1)):
                children.append(random_comparison_expression(random_str(), random_str()))

            expr_obj = getattr(qubu, expr)(*children)
            expected = {f'${expr.lower()}': [c.compile() for c in children]}
            assert expr_obj.compile() == expected

        # Test 'Not' expression
        f_name, arg = random_str(), random_str()
        comp_expr = random_comparison_expression(f_name, arg)

        assert qubu.Not(comp_expr).compile() == {f_name: {'$not': {comp_expr.name: arg}}}

    def test_evaluation_expressions(self):
        # Test Text expression
        search = random_str()
        lang = random.choice(SUPPORTED_LANGS)
        case_sens = random.choice([True, False])
        diac_sens = random.choice([True, False])
        expected = {'$text': {
            '$search': search,
            '$language': lang,
            '$caseSensitive': case_sens,
            '$diacriticSensitive': diac_sens,
        }}
        expr = qubu.Text(search=search, language=lang, case_sensitive=case_sens, diacritic_sensitive=diac_sens)
        assert expr.compile() == expected

        # Text Text expression with unsupported language
        expected = {'$text': {
            '$search': search,
            '$language': 'none',
            '$caseSensitive': case_sens,
            '$diacriticSensitive': diac_sens,
        }}
        expr = qubu.Text(search=search, language=random_str(), case_sensitive=case_sens, diacritic_sensitive=diac_sens)
        assert expr.compile() == expected

        # Test Text expression exceptions
        with pytest.raises(ValueError):
            qubu.Text()

        # Test Regex expression
        f_name = random_str()
        pattern = random_str()
        expected = {f_name: {
            '$regex': pattern,
            '$options': 'imsv',
        }}
        expr = qubu.Regex(f_name, pattern=pattern, i=True, m=True, s=True, v=True)
        assert expr.compile() == expected

        # Test Regex expression exceptions
        with pytest.raises(ValueError):
            qubu.Regex(f_name)

    def test_geospatial_expressions(self):
        # Test Near expression
        f_name = random_str()
        lng = random.random() * 100
        lat = random.random() * 100
        min_d = random.randrange(0, 10000)
        max_d = random.randrange(0, 10000)
        for op in ('Near', 'NearSphere'):
            expr = getattr(qubu, op)(f_name, lng=lng, lat=lat, min_distance=min_d, max_distance=max_d)
            expected = {f_name: {expr.name: {
                '$geometry': {
                    'type': 'Point',
                    'coordinates': [lng, lat],
                },
                '$minDistance': min_d,
                '$maxDistance': max_d,
            }}}
            assert expr.compile() == expected

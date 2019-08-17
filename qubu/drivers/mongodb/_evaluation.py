"""Database Query Builder
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from qubu import contract
from ._expression import MongoDBExpression

SUPPORTED_LANGS = ('da', 'nl', 'en', 'fi', 'fr', 'de', 'hu', 'it', 'nb', 'pt', 'ro', 'ru', 'es', 'sv', 'tr',
                    'ara', 'prs', 'pes', 'urd', 'zhs', 'zht')


class Text(MongoDBExpression, contract.Text):
    """Text Search
    """

    def __init__(self, **kwargs):
        """Init
        """
        super().__init__(**kwargs)

        self._search = kwargs.get('search')
        if not self._search:
            raise ValueError("'search' keyword argument is required")

        self._language = kwargs.get('language')
        self._case_sensitive = kwargs.get('case_sensitive', False)
        self._diacritic_sensitive = kwargs.get('diacritic_sensitive', False)

        if self._language not in SUPPORTED_LANGS:
            self._language = 'none'

    def compile(self) -> dict:
        """Get representation of operator's content
        """

        return {
            '$text': {
                '$search': str(self._search),
                '$language': self._language,
                '$caseSensitive': self._case_sensitive,
                '$diacriticSensitive': self._diacritic_sensitive,
            }
        }


class Regex(MongoDBExpression, contract.Regex):
    """Pattern Matching Expression
    """

    def __init__(self, field: str, **kwargs):
        """Init
        """
        super().__init__(field, **kwargs)

        self._pattern = kwargs.get('pattern')
        if not self._pattern:
            raise ValueError("'pattern' keyword argument is required")

        self._options = ''

        for opt in 'imsv':
            if kwargs.get(opt):
                self._options += opt

    def compile(self) -> dict:
        """Compile the expression
        """
        r = {
            self._field: {
                '$regex': str(self._pattern),
            }
        }

        if self._options:
            r[self._field]['$options'] = self._options

        return r

from pygments.lexer import RegexLexer
from pygments.token import *

class EucalyptLexer(RegexLexer):

    name = 'Eucalypt'
    aliases = ['eucalypt', 'eu']
    filenames = ['*.eu']

    block_anaphora = "•\d*"
    expression_anaphora = "_\d*"
    identifier = "[•$?_a-zA-Zα-ω][•$?_*a-zA-Z0-9\-α-ω]*"
    operator = r'[!@£%^&*|></+=-~\-∧∨∘][!@£%^&*|></+=~\-]*'
    number_float = r'[+-]?\d+(\.\d+)?'
    number_int = r'[+-]?\d+'

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'"[^"]*"', String),
            (r'#.*?$', Comment),
            (r':\'[^\']+\'', String.Symbol),
            (r':' + identifier, String.Symbol),
            (r':', Punctuation),
            (r',', Punctuation),
            (r'`', Keyword),
            (r'\'[^\']+\'', String.Name),
            (r'[{}\[\]\(\)]', Punctuation),
            (r'__' + identifier, Name.Builtin),
            (block_anaphora, Name.Builtin.Pseudo),
            (expression_anaphora, Name.Builtin.Pseudo),
            (identifier, Name),
            (operator, Operator),
            (r'\.', Operator),
            (number_float, Number.Float),
            (number_int, Number.Int),
        ]
    }

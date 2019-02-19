from setuptools import setup

__author__ = 'Greg Hawkins <greg@curvelogic.co.uk>'

__doc__ = """\ A pygments lexer for the eucalypt language
(http://curvelogic.co.uk/eucalypt). """

setup(
    name='Eucalypt Pygments Lexer',
    version='0.1.0dev',
    description=__doc__,
    author=__author__,
    packages=['eucalypt_lexer'],
    entry_points='''[pygments.lexers]
eucalypt = eucalypt_lexer:EucalyptLexer
'''
)

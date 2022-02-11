from typing import NamedTuple
import re


class Token(NamedTuple):
    type: str
    value: str


def tokenize(code):
    ret = []
    errors = []
    keywords = {'print', 'if', 'else', 'for', 'Next', 'Student', 'Element', 'Activity', 'Simulate', 'Rule',
                'return', 'SetRule', '<=', '>=', '==', '!=', '<', '>', 'and', 'or'}
    token_specification = [

        ('comment', r'[\#](\w+)#|[\#](\w+)[ \t]+(\w+)#|'),      # comment
        ('true', r'True'),             # true
        ('false', r'False'),           # false
        ('string', r'[\"](\w+)[\"]|[\"](\w+)[ \t]+(\w+)[\"]'),  # string
        ('return', r'return'),         # return
        ('eof', r'eof'),               # eof
        ('let', r'let'),               # let
        ('for', r'for'),               # for
        ('if', r'if'),                 # if
        ('else', r'else'),             # else
        ('def', r'def'),               # def
        ('Student', r'Student'),       # Student
        ('Element', r'Element'),       # Element

        # Comparison operators
        ('leq', r'<='),                # less than or equal
        ('geq', r'>='),                # greater than or equal
        ('equal', r'=='),              # equal
        ('not', r'!='),                # not equal
        ('less', r'[<]'),              # less than
        ('greater', r'[>]'),           # greater than

        ('o_bracket', r'\('),          # (
        ('c_bracket', r'\)'),          # )

        ('o_key', r'\{'),               # {
        ('c_key', r'\}'),               # }

        ('comma', r','),               # comma
        ('colon', r':'),               # colon

        # Logic operators
        ('and', r'and'),               # and
        ('or', r'or'),                 # or

        ('print', r'print'),           # print

        ('number', r'\d+(\.\d*)?'),    # Integer or decimal number
        ('assign', r'='),              # Assignment operator
        ('semi', r';'),                # ;
        ('id', r'[A-Za-z]+'),          # Identifiers

        # Arithmetic operators
        ('plus', r'[+]'),              # plus
        ('minus', r'[\-]'),            # minus
        ('mul', r'[*]'),               # mul
        ('div', r'[/]'),               # div

        ('newline',  r'\n'),           # Line endings
        ('skip',     r'[ \t]+'),
        ('salt', r'\r'),       # Skip over spaces and tabs
        ('mismatch', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    code += ' eof'
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'number':
            value = float(value) if '.' in value else int(value)
        elif kind == 'true' or kind == 'false':
            value = eval(value)
        elif kind == 'id' and value in keywords:
            kind = value
        elif kind == 'newline' or kind == 'comment' or kind == 'skip' or kind == 'salt':
            continue
        elif kind == 'mismatch':
            errors.append(f'{value} expresión no reconocida en el lenguaje')
            continue
        ret.append(Token(kind, value))
    return errors, ret




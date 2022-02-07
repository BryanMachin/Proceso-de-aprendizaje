from typing import NamedTuple
import re


class Token(NamedTuple):
    type: str
    value: str


def tokenize(code):
    ret = []
    keywords = {'print', 'if', 'else', 'for', 'Next', 'Student', 'Element', 'Activity', 'Simulate', 'Rule',
                'Return', 'SetRule', '<=', '>=', '==', '!=', '<', '>', 'and', 'or'}
    token_specification = [
        ('eof', r'eof'),               # eof
        ('let', r'let'),               # let
        ('for', r'for'),               # for
        ('if', r'eof'),                # if
        ('then', 'then'),              # then
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

        ('o_bracket', r'\('),           # (
        ('c_bracket', r'\)'),           # )

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
        ('skip',     r'[ \t]+'),       # Skip over spaces and tabs
        ('mismatch', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    code += ' eof'
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'number':
            value = float(value) if '.' in value else int(value)
        elif kind == 'id' and value in keywords:
            kind = value
        elif kind == 'newline':
            continue
        elif kind == 'skip':
            continue
        elif kind == 'mismatch':
            raise RuntimeError(f'{value!r} unexpected')
        ret.append(Token(kind, value))
    return ret


statements = '''
    If quantity  and 5 == 4 or 5 >= 6 Then
        total = total + price * quantity;
        tax = price * 0.05;
    EndIf;
'''



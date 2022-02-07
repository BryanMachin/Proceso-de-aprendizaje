
class Token:
    def __init__(self, _type, value, location):
        self._type = _type
        self.value = value
        self.location = location
    
    def __str__(self):
        return self._type + "[" + self.value + "]"

    def type(self):
        return self._type

    def value(self):
        return self.value

    def location(self):
        return self.location


class TokenType:
    Unknown = "Unknown"
    Number = "Number"
    Text = "Text"
    Keyword = "Keyword"
    Identifier = "Identifier"
    Symbol = "Symbol"


class TokenValue:
    Add = "Add"
    Sub = "Sub"
    Mul = "Mul"
    Div = "Div"
    Mod = "Mod"
    Less = "Less"
    LessOrEquals = "LEqual"

    If = "IfClausule"
    Then = "ThenClausule"
    Else = "ElseClausule"


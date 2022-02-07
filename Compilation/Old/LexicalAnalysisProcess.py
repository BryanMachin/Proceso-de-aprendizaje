

class LexicalAnalyzer:

    # Variables
    operators = dict()
    keywords = dict()
    comments = dict()
    texts = dict()

    # RegisterMethods
    def register_operator(self, op, token_value):
        self.operators[op] = token_value

    def register_keywords(self, kw, token_value):
        self.keywords[kw] = token_value

    def register_comment(self, start, end):
        self.comments[start] = end

    def __match_comment(self, stream, errors):
        pass


class TokenReader:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.line = 1
        self.lastLB = -1
    
    def peek(self):
        if self.pos < 0 or self.pos >= len(self.code):
            Exception()
        return self.code[self.pos]
    
    def eof(self):
        return self.pos >= len(self.code)
    
    def eol(self):
        return self.eof() or self.code[self.pos] == '\n'
    
    def continues_with(self, prefix):
        if self.pos + len(prefix) > len(self.code):
            return False
        for i in range(len(prefix)):
            if self.code[self.pos + i] != prefix[i]:
                return False
        return True
    
    def match(self, prefix):
        if self.continues_with(prefix):
            self.pos += len(prefix)
            return True
        return False

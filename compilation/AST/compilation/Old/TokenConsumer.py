import compilation.Old.Token


class TokenConsumer:
    def __init__(self, tokens: Token):
        self.tokens = tokens
        self.position = 0
    
    def end_of_tokens(self):
        return self.position == len(self.tokens)

    def current(self):
        return self.tokens[self.position]

    def next(self):
        if self.position < len(self.tokens):
            self.position += 1
        return self.position < len(self.tokens)

    def cant_look_ahead(self, k: int):
        return len(self.tokens) - self.position > k

    def look_ahead(self, k: int):
        return self.tokens[self.position + k]

    def get_enumerator(self):
        for i in self.tokens:
            yield i

    def position(self):
        return self.position




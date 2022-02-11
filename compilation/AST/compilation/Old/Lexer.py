from compilation.Old.Token import *
from compilation.Old.LexicalAnalysisProcess import *
from compilation.Old.TokenConsumer import *


class Lexer:
    def __init__(self):
        self.lexicalAnalyzer = LexicalAnalyzer()

        # Keywords
        self.lexicalAnalyzer.RegisterKeyword("if", TokenValue.If)

        # Operators
        self.lexicalAnalyzer.RegisterOperator("+", TokenValue.Add)

        # Comments
        self.lexicalAnalyzer.RegisterComment("#")

    def __init__(self, output_info):
        self.outputInfo = output_info

    def lexical_analyzer(self):
        return self.lexicalAnalyzer


    def get_token_consumer(self, code):
        errors = []
        tokens = self.lexicalAnalyzer.GetTokens(code, errors)
        for i in errors:
            self.outputInfo.AddError(i)
        return TokenConsumer(tokens)
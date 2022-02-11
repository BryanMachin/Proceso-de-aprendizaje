

class Symbol(object):
    def __init__(self, name, grammar):
        self.name = name
        self.grammar = grammar

    def __repr__(self):
        return repr(self.name)

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Symbol):
            return Sentence(self, other)
        raise TypeError(other)

    def __or__(self, other):
        if isinstance(other, Sentence):
            return SentenceList(Sentence(self), other)
        raise TypeError(other)

    def __len__(self):
        return 1

    @property
    def is_epsilon(self):
        return False


class Sentence(object):
    def __init__(self, *args):
        self._symbols = tuple(x for x in args if not x.is_epsilon)
        self.hash = hash(self._symbols)

    def __len__(self):
        return len(self._symbols)

    def __add__(self, other):
        if isinstance(other, Symbol):
            return Sentence(*(self._symbols + (other,)))
        if isinstance(other, Sentence):
            return Sentence(*(self._symbols + other._symbols))

    def __or__(self, other):
        if isinstance(other, Sentence):
            return SentenceList(self, other)
        if isinstance(other, Symbol):
            return SentenceList(self, Sentence(other))

    def __str__(self):
        return ("%s " * len(self._symbols) % tuple(self._symbols)).strip()

    def __iter__(self):
        return iter(self._symbols)

    def __getitem__(self, index):
        return self._symbols[index]

    def __eq__(self, other):
        return self._symbols == other._symbols

    def __hash__(self):
        return self.hash

    @property
    def is_epsilon(self):
        return False


class SentenceList(object):
    def __init__(self, *args):
        self._sentences = list(args)

    def add(self, symbol):
        if not symbol and (symbol is None or not symbol.is_epsilon):
            raise ValueError(symbol)
        self._sentences.append(symbol)

    def __or__(self, other):
        if isinstance(other, Sentence):
            self.add(other)
            return self

        if isinstance(other, Symbol):
            return self | Sentence(other)

    def __iter__(self):
        return iter(self._sentences)


class Production(object):
    def __init__(self, non_terminal, sentence):
        self.Left = non_terminal
        self.Right = sentence

    def __str__(self):
        return '%s := %s' % (self.Left, self.Right)

    def __repr__(self):
        return '%s -> %s' % (self.Left, self.Right)

    def __iter__(self):
        yield self.Left
        yield self.Right

    def __eq__(self, other):
        return isinstance(other, Production) and self.Left == other.Left and self.Right == other.Right

    def __hash__(self):
        return hash((self.Left, self.Right))

    @property
    def is_epsilon(self):
        return self.Right.IsEpsilon


class AttributeProduction(Production):
    def __init__(self, non_terminal, sentence, attributes):
        if not isinstance(sentence, Sentence) and isinstance(sentence, Symbol):
            sentence = Sentence(sentence)
        super(AttributeProduction, self).__init__(non_terminal, sentence)
        self.attributes = attributes

    def __str__(self):
        return '%s := %s' % (self.Left, self.Right)

    def __repr__(self):
        return '%s -> %s' % (self.Left, self.Right)

    def __iter__(self):
        yield self.Left
        yield self.Right

    @property
    def is_epsilon(self):
        return self.Right.IsEpsilon


class NonTerminal(Symbol):
    def __init__(self, name, grammar):
        super().__init__(name, grammar)
        self.Productions = []

    def __str__(self):
        return self.name

    def __mod__(self, other):
        if isinstance(other, Sentence):
            p = Production(self, other)
            self.grammar.add_production(p)
            return self
        if isinstance(other, tuple):
            if len(other) == 2:
                other += (None,) * len(other[0])
            # Debe definirse una regla por cada símbolo de la producción
            if isinstance(other[0], Symbol) or isinstance(other[0], Sentence):
                p = AttributeProduction(self, other[0], other[1:])
            else:
                raise Exception("")
            self.grammar.add_production(p)
            return self
        if isinstance(other, Symbol):
            p = Production(self, Sentence(other))
            self.grammar.add_production(p)
            return self
        if isinstance(other, SentenceList):
            for s in other:
                p = Production(self, s)
                self.grammar.add_production(p)
            return self
        raise TypeError(other)

    @property
    def is_terminal(self):
        return False

    @property
    def is_non_terminal(self):
        return True

    @property
    def is_epsilon(self):
        return False


class Terminal(Symbol):
    def __int__(self, name, grammar):
        super().__init__(name, grammar)
        self.Productions = []

    def __str__(self):
        return self.name

    @property
    def is_terminal(self):
        return True

    @property
    def is_non_terminal(self):
        return False

    @property
    def is_epsilon(self):
        return False


class EOF(Terminal):
    def __init__(self, grammar):
        super().__init__('eof', grammar)

    def __str__(self):
        return 'eof'


class Epsilon(Terminal, Sentence):
    def __init__(self, grammar):
        super().__init__('epsilon', grammar)

    def __hash__(self):
        return hash("")

    def __len__(self):
        return 0

    def __str__(self):
        return "e"

    def __repr__(self):
        return 'epsilon'

    def __iter__(self):
        yield from ()

    def __add__(self, other):
        return other

    def __eq__(self, other):
        return isinstance(other, (Epsilon,))

    @property
    def is_epsilon(self):
        return True


class Grammar:
    def __init__(self):
        self.Productions = []
        self.pType = None
        self.Non_terminals = []
        self.Terminals = []
        self.Start_symbol = None
        self.Epsilon = Epsilon(self)
        self.Eof = EOF(self)
        self.SymbolDict = {'eof': self.Eof}

    def non_terminal(self, name, start_symbol=False):
        if not name:
            raise Exception("Empty")
        term = NonTerminal(name, self)
        if start_symbol:
            if self.Start_symbol is None:
                self.Start_symbol = term
            else:
                raise Exception('Cannot define more than one start symbol')
        self.Non_terminals.append(term)
        self.SymbolDict[name] = term
        return term

    def non_terminals(self, names):
        aux = tuple(self.non_terminal(i) for i in names.strip().split())
        return aux

    def add_production(self, production):
        if len(self.Productions) == 0:
            self.pType = type(production)
        production.Left.Productions.append(production)
        self.Productions.append(production)

    def terminal(self, name):
        if not name:
            raise Exception('Empty')
        term = Terminal(name, self)
        self.Terminals.append(term)
        self.SymbolDict[name] = term
        return term

    def terminals(self, names):
        aux = tuple(self.terminal(i) for i in names.strip().split())
        return aux

    def __getitem__(self, item):
        try:
            return self.SymbolDict[item]
        except KeyError:
            return None

    def copy(self):
        g = Grammar()
        g.Productions = self.Productions.copy()
        g.Non_terminals = self.Non_terminals.copy()
        g.Terminals = self.Terminals.copy()
        g.pType = self.pType
        g.Start_symbol = self.Start_symbol
        g.Epsilon = self.Epsilon
        g.Eof = self.Eof
        g.SymbolDict = self.SymbolDict.copy()
        return g

    @property
    def is_augmented_grammar(self):
        augmented = 0
        for left, right in self.Productions:
            if self.Start_symbol == left:
                augmented += 1
        if augmented <= 1:
            return True
        else:
            return False

    def augmented_grammar(self, force=False):
        if not self.is_augmented_grammar or force:
            g = self.copy()
            s = g.Start_symbol
            g.Start_symbol = None
            ss = g.non_terminal('S\'', True)
            if g.pType is AttributeProduction:
                ss %= s + g.Epsilon, lambda x: x
            else:
                ss %= s + g.Epsilon
            return g
        else:
            return self.copy()


class Item:
    def __init__(self, production, pos, lookaheads=frozenset()):
        self.Production = production
        self.Pos = pos
        self.Lookaheads = frozenset(look for look in lookaheads)

    def __str__(self):
        s = str(self.Production.Left) + " -> "
        if len(self.Production.Right) > 0:
            for i, c in enumerate(self.Production.Right):
                if i == self.Pos:
                    s += "."
                s += str(self.Production.Right[i])
            if self.Pos == len(self.Production.Right):
                s += "."
        else:
            s += "."
        s += ", " + str(self.Lookaheads)[10:-1]
        return s

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (
                (self.Pos == other.Pos) and
                (self.Production == other.Production) and
                (set(self.Lookaheads) == set(other.Lookaheads))
        )

    def __hash__(self):
        return hash((self.Production, self.Pos, self.Lookaheads))

    @property
    def is_reduce_item(self):
        return len(self.Production.Right) == self.Pos

    @property
    def next_symbol(self):
        if self.Pos < len(self.Production.Right):
            return self.Production.Right[self.Pos]
        else:
            return None

    def next_item(self):
        if self.Pos < len(self.Production.Right):
            return Item(self.Production, self.Pos + 1, self.Lookaheads)
        else:
            return None

    def preview(self, skip=1):
        return [ self.Production.Right[self.Pos + skip:] + (lookahead,) for lookahead in self.Lookaheads]

    def center(self):
        return Item(self.Production, self.Pos)

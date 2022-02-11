from compilation.Parser.Grammar import *
from compilation.Parser.Tools import *
from compilation.Parser.Parser_LR1 import *

G = Grammar()
E = G.non_terminal('E', True)
T, F, X, Y = G.non_terminals('T F X Y')
plus, minus, star, div, opar, cpar, num = G.terminals('+ - * / ( ) num')

E %= T + X
X %= plus + T + X | minus + T + X | G.Epsilon
T %= F + Y
Y %= star + F + Y | div + F + Y | G.Epsilon
F %= num | opar + E + cpar

firsts = compute_firsts(G)


def closure_lr1(self, items, firsts):
    closure = ContainerSet(*items)

    changed = True
    while changed:
        new_items = ContainerSet()
        # por cada item hacer expand y añadirlo a new_items
        for item in closure:
            e = self.expand(item, firsts)
            new_items.extend(e)
        changed = closure.update(new_items)
    return self.compress(closure)


def compress(self, items):
    centers = {}
    for item in items:
        center = item.center()
        try:
            lookaheads = centers[center]
        except KeyError:
            centers[center] = lookaheads = set()
        lookaheads.update(item.Lookaheads)
    return {Item(x.Production, x.pos, set(lookahead)) for x, lookahead in centers.items()}


def expand(self, item, firsts):
    next_symbol = item.NextSymbol
    if next_symbol is None or not next_symbol.IsNonTerminal:
        return []
    lookaheads = ContainerSet()
    #  (Compute lookahead for child items)
    # calcular el first a todos los preview posibles
    for p in item.Preview():
        for first in compute_local_first(firsts, p):
            lookaheads.add(first)
    assert not lookaheads.contains_epsilon
    #  (Build and return child items)
    _list = []
    for production in next_symbol.productions:
        _list.append(Item(production, 0, lookaheads))
    return _list


item = Item(E.productions[0], 0, lookaheads=[G.Eof, plus])

closure = closure_lr1([item, item.next_item().next_item()], firsts)
for x in closure:
    print(x)

a = 1

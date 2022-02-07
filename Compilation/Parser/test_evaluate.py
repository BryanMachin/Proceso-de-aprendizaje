from Grammar import *
from AST.Evaluate import *
from Parser.Parser_LR1 import LR1Parser
from Tokenizer.Tokenizer import tokenize
from AST.Nodes import *

g = Grammar()

program = g.non_terminal('<program>', start_symbol=True)
stat_list, stat = g.non_terminals('<stat_list> <stat>')
let_var, def_func, print_stat, arg_list = g.non_terminals('<let-var> <def-func> <print-stat> <arg-list>')
expr, term, factor, atom = g.non_terminals('<expr> <term> <factor> <atom>')
func_call, expr_list = g.non_terminals('<func-call> <expr-list>')

let, defx, printx = g.terminals('let def print')
semi, comma, opar, cpar, colon = g.terminals('semi comma o_bracket c_bracket colon')
equal, plus, minus, star, div = g.terminals('assign plus minus mul div')
idx, num = g.terminals('id number')

program %= stat_list, lambda h, s: ProgramNode(s[1])

stat_list %= stat + semi, lambda h, s: [s[1]]
stat_list %= stat + semi + stat_list, lambda h, s: [s[1]] + s[3]

stat %= let_var, lambda h, s: s[1]
stat %= def_func, lambda h, s: s[1]
stat %= print_stat, lambda h, s: s[1]

print_stat %= printx + expr, lambda h, s: PrintNode(s[2])

let_var %= let + idx + equal + expr, lambda h, s: VarDeclarationNode(s[2], s[4])

def_func %= defx + idx + opar + arg_list + cpar + colon + expr, lambda h, s: FuncDeclarationNode(s[2], s[4], s[7])

arg_list %= idx, lambda h, s: [s[1]]
arg_list %= idx + comma + arg_list, lambda h, s: [s[1]] + s[3]

expr %= expr + plus + term, lambda h, s: PlusNode(s[1], s[3])
expr %= expr + minus + term, lambda h, s: MinusNode(s[1], s[3])
expr %= term, lambda h, s: s[1], None

term %= term + star + factor, lambda h, s: StarNode(s[1], s[3])
term %= term + div + factor, lambda h, s: DivNode(s[1], s[3])
term %= factor, lambda h, s: s[1]

factor %= atom, lambda h, s: s[1]
factor %= opar + expr + cpar, lambda h, s: s[2]

atom %= num, lambda h, s: ConstantNumNode(s[1])
atom %= idx, lambda h, s: VariableNode(s[1])
atom %= func_call, lambda h, s: s[1]

func_call %= idx + opar + expr_list + cpar, lambda h, s: CallNode(s[1], s[3])

expr_list %= expr, lambda h, s: [s[1]]
expr_list %= expr + comma + expr_list, lambda h, s: [s[1]] + s[3]


parser = LR1Parser(g)


p = '''print 1 - 1 - 1;
let x = 58;
def f ( a, b ) : 5 + 6;
print F( 5 + x, 7 + y );
'''

tokens = tokenize(p)

parse, operations = parser([i.type for i in tokens], ope=True)

ast = evaluate_reverse_parse(parse, operations, tokens)

print(ast)

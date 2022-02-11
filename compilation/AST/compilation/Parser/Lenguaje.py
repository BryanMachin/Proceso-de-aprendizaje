from compilation.Parser.Grammar import *
from compilation.AST.Construction import *
from compilation.Parser.Parser_LR1 import LR1Parser
from compilation.Tokenizer.Tokenizer import tokenize
from compilation.AST.Nodes import *
from compilation.AST.Context import *

g = Grammar()

program = g.non_terminal('<program>', start_symbol=True)
stat_list, stat = g.non_terminals('<stat_list> <stat>')
let_var, def_func, print_stat, arg_list, def_return = \
    g.non_terminals('<let-var> <def-func> <print-stat> <arg-list> <def-return>')
expr, term, factor, atom = g.non_terminals('<expr> <term> <factor> <atom>')
func_call, expr_list = g.non_terminals('<func-call> <expr-list>')
if_decl, if_else_decl, for_decl = g.non_terminals('<if-decl> <if-else-decl> <for_decl>')

ifx, elsex, let, defx, printx, returnx = g.terminals('if else let def print return')
semi, comma, opar, cpar, colon, okey, ckey = g.terminals('semi comma o_bracket c_bracket colon o_key c_key')
equal, plus, minus, star, div, andx, orx, true, false = g.terminals('assign plus minus mul div and or true false')
leq, geq, equalx, notx, less, greater = g.terminals('leq geq equal not less greater')
idx, num, stringx, forx = g.terminals('id number string for')

program %= stat_list, lambda h, s: ProgramNode(s[1])

stat_list %= stat, lambda h, s: [s[1]]
stat_list %= stat + stat_list, lambda h, s: [s[1]] + s[2]

stat %= let_var + semi, lambda h, s: s[1]
stat %= def_func, lambda h, s: s[1]
stat %= print_stat + semi, lambda h, s: s[1]
stat %= if_decl, lambda h, s: s[1]
stat %= if_else_decl, lambda h, s: s[1]
stat %= def_return + semi, lambda h, s: s[1]
stat %= for_decl, lambda h, s: s[1]

if_decl %= ifx + opar + expr + cpar + okey + stat_list + ckey, lambda h, s: IfExprNode(s[3], s[6])
if_else_decl %= ifx + opar + expr + cpar + okey + stat_list + ckey + elsex + okey + stat_list + ckey, \
                lambda h, s: IfElseExprNode(s[3], s[6], s[10])

for_decl %= forx + opar + idx + equal + num + semi + expr + semi + idx + plus + plus + cpar + okey + stat_list + ckey, \
            lambda h, s: ForNode(s[3], s[5], s[7], s[9], s[10], s[11], s[14])

def_return %= returnx + expr, lambda h, s: ReturnNode(s[2])

print_stat %= printx + expr, lambda h, s: PrintNode(s[2])

let_var %= let + idx + equal + expr, lambda h, s: VarDeclarationNode(s[2], s[4])

def_func %= defx + idx + opar + arg_list + cpar + okey + stat_list + ckey, \
            lambda h, s: FuncDeclarationNode(s[2], s[4], s[7])

arg_list %= idx, lambda h, s: [s[1]]
arg_list %= idx + comma + arg_list, lambda h, s: [s[1]] + s[3]


expr %= expr + plus + term, lambda h, s: PlusNode(s[1], s[3])
expr %= expr + minus + term, lambda h, s: MinusNode(s[1], s[3])
term %= term + star + factor, lambda h, s: StarNode(s[1], s[3])
term %= term + div + factor, lambda h, s: DivNode(s[1], s[3])

expr %= expr + leq + term, lambda h, s: LeqNode(s[1], s[3])
expr %= expr + geq + term, lambda h, s: GeqNode(s[1], s[3])
expr %= expr + equalx + term, lambda h, s: EqualNode(s[1], s[3])
expr %= expr + notx + term, lambda h, s: NotNode(s[1], s[3])
expr %= expr + less + term, lambda h, s: LessNode(s[1], s[3])
expr %= expr + greater + term, lambda h, s: GreaterNode(s[1], s[3])

expr %= expr + andx + term, lambda h, s: AndNode(s[1], s[3])
expr %= expr + orx + term, lambda h, s: OrNode(s[1], s[3])

expr %= term, lambda h, s: s[1], None


term %= factor, lambda h, s: s[1]
factor %= atom, lambda h, s: s[1]
factor %= opar + expr + cpar, lambda h, s: s[2]


atom %= stringx, lambda h, s: ConstantStrNode(s[1])
atom %= num, lambda h, s: ConstantNumNode(s[1])
atom %= true, lambda h, s: ConstantBoolNode(s[1])
atom %= false, lambda h, s: ConstantBoolNode(s[1])
atom %= idx, lambda h, s: VariableNode(s[1])
atom %= func_call, lambda h, s: s[1]

func_call %= idx + opar + expr_list + cpar, lambda h, s: CallNode(s[1], s[3])

expr_list %= expr, lambda h, s: [s[1]]
expr_list %= expr + comma + expr_list, lambda h, s: [s[1]] + s[3]


parser = LR1Parser(g)


p = '''
let x = 20; 
let y = x * 50; 
print y + 15 / 3 - 1;
'''

h = ''' 
def COMP(x,y) {
    return x < y; 
 } 
 print COMP(4,5);
 '''

fac = '''
def fac(n){
    if(n <= 1){
        let x = 1;
    }
    else{
        let x = n*fac(n-1);
    }    
    return x;
}
print fac(5);
'''

fib = ''' 
def fib(n){
    if(n < 2){
    let x = n;
    }
    else{
        let x = fib(n-1) + fib(n-2);
    }
    return x;
} 
print fib(12);
'''

f = '''
def SUM(x,y){
let z = 50;
 return x+z;
 }

if (3 < 2 or False and True){
print "Hello";
}
else{
print SUM(4,5);
}
 '''

d = ''' 
let x = 58;
def f ( a, b ){
 return 5 + 6;
 }
print f( 5 + x, 7 );
 '''

s = '''
print " # Hello Bryan";
'''

k = '''
print 2 + 7 * 5 / 7;
'''

b = ''' 
hfh #False True#
'''
g = '''
print 0 and True;
'''

forx = '''
let i = 15;
for(i = 0; i < 10;i++){
print i;
}
'''

errors_tokenizer, tokens = tokenize(forx)

print(errors_tokenizer)

errors, parse, operations = parser([i.type for i in tokens], ope=True)


def errors_parser(errors, tokens):
    err = []
    for i in errors:
        value = ''
        for t in tokens:
            if t.type == i:
                value = t.value
                break
        err.append(f'{i} -> {value} no ha sido bien definido :(')
    return err


print(errors_parser(errors, tokens))

ast = construction_ast(parse, operations, tokens)

errors_ast, answer = ast.run()

print(errors_ast)

print(answer)


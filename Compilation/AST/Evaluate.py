from Parser.ShiftReduce import ShiftReduce


def evaluate_reverse_parse(parser_lr1, operations, tokens):
    if not parser_lr1 or not operations or not tokens:
        return  # Nada que eval!!!!
    right_parse = iter(parser_lr1)
    tokens = iter(tokens)
    stack = []
    for operation in operations:
        if operation == ShiftReduce.SHIFT:
            token = next(tokens)
            stack.append(token.value)
        elif operation == ShiftReduce.REDUCE:
            production = next(right_parse)
            head, body = production
            attributes = production.attributes
            assert all(rule is None for rule in attributes[1:]), 'There must be only synteticed attributes.'
            rule = attributes[0]
            if len(body):
                synteticed = [None] + stack[-len(body):]
                value = rule(None, synteticed)
                stack[-len(body):] = [value]
            else:
                stack.append(rule(None, None))
        else:
            raise Exception('error')
    assert len(stack) == 1 and next(tokens).type == 'eof', 'el token final no es eof'
    return stack[0]

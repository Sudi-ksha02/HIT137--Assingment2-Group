def parse_term(tokens):
    """term → unary (('' | '/') unary)"""
    left, tokens = parse_unary(tokens)

    while tokens[0]['type'] == 'OP' and tokens[0]['value'] in ('*', '/'):
        op = tokens[0]['value']
        tokens = tokens[1:]
        right, tokens = parse_unary(tokens)
        left = (op, left, right)

    return left, tokens


def parse_unary(tokens):
    """unary → '-' unary | primary"""
    if tokens[0]['type'] == 'OP' and tokens[0]['value'] == '-':
        tokens = tokens[1:]
        operand, tokens = parse_unary(tokens)
        return ('neg', operand), tokens

    # Unary + is NOT supported
    if tokens[0]['type'] == 'OP' and tokens[0]['value'] == '+':
        raise ParseError("Unary + is not supported")

    return parse_primary(tokens)
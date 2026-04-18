def parse_primary(tokens):
    """primary → NUM | '(' expr ')'"""
    tok = tokens[0]

    if tok['type'] == 'NUM':
        return tok['value'], tokens[1:]

    if tok['type'] == 'LPAREN':
        tokens = tokens[1:]  # consume '('
        inner, tokens = parse_expr(tokens)
        if tokens[0]['type'] != 'RPAREN':
            raise ParseError("Expected ')'")
        tokens = tokens[1:]  # consume ')'
        return inner, tokens

    raise ParseError(f"Unexpected token in primary: {tok}")





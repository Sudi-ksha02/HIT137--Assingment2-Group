def tokenise(expression):
    """
    Convert an expression string into a list of token dicts.
    Each token: {'type': str, 'value': str|int|float}

    Token types: NUM, OP, LPAREN, RPAREN, END
    Returns None on error (unknown character).
    """
    tokens = []
    i = 0
    s = expression.strip()

    while i < len(s):
        ch = s[i]

        if ch.isspace():
            i += 1
            continue

        if ch.isdigit() or (ch == '.' and i + 1 < len(s) and s[i+1].isdigit()):
            j = i
            while j < len(s) and (s[j].isdigit() or s[j] == '.'):
                j += 1
            num_str = s[i:j]
            val = float(num_str)
            tokens.append({'type': 'NUM', 'value': val})
            i = j
            continue

        if ch in '+-*/':
            tokens.append({'type': 'OP', 'value': ch})
            i += 1
            continue

        if ch == '(':
            tokens.append({'type': 'LPAREN', 'value': '('})
            i += 1
            continue

        if ch == ')':
            tokens.append({'type': 'RPAREN', 'value': ')'})
            i += 1
            continue

        # Unknown character → error
        return None

    tokens.append({'type': 'END', 'value': 'END'})
    return tokens
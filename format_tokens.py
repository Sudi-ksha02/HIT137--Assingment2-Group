def format_tokens(tokens):
    """Format token list as the required output string."""
    parts = []
    for t in tokens:
        if t['type'] == 'NUM':
            v = t['value']
            # Display as int if whole number
            display = str(int(v)) if v == int(v) else str(v)
            parts.append(f"[NUM:{display}]")
        elif t['type'] == 'OP':
            parts.append(f"[OP:{t['value']}]")
        elif t['type'] == 'LPAREN':
            parts.append(f"[LPAREN:{t['value']}]")
        elif t['type'] == 'RPAREN':
            parts.append(f"[RPAREN:{t['value']}]")
        elif t['type'] == 'END':
            parts.append("[END]")
    return ' '.join(parts)
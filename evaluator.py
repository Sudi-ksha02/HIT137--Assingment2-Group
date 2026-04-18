
import os
import math



def tokenise(expression):
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



class ParseError(Exception):
    pass


def parse(tokens):
    """Entry point. Returns (tree, remaining_tokens). Raises ParseError on failure."""
    tree, tokens = parse_expr(tokens)
    if tokens[0]['type'] != 'END':
        raise ParseError(f"Unexpected token: {tokens[0]}")
    return tree


def parse_expr(tokens):
    """expr → term (('+' | '-') term)*"""
    left, tokens = parse_term(tokens)

    while tokens[0]['type'] == 'OP' and tokens[0]['value'] in ('+', '-'):
        op = tokens[0]['value']
        tokens = tokens[1:]
        right, tokens = parse_term(tokens)
        left = (op, left, right)

    return left, tokens


def parse_term(tokens):
    """term → unary (('*' | '/') unary)*"""
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




def tree_to_str(tree):
    """Convert parse tree to prefix-notation string."""
    if isinstance(tree, (int, float)):
        v = tree
        return str(int(v)) if v == int(v) else str(round(v, 4))

    if isinstance(tree, tuple):
        if tree[0] == 'neg':
            return f"(neg {tree_to_str(tree[1])})"
        else:
            op, left, right = tree
            return f"({op} {tree_to_str(left)} {tree_to_str(right)})"

    return str(tree)




def evaluate_tree(tree):
    """Evaluate a parse tree. Raises ZeroDivisionError or ValueError on failure."""
    if isinstance(tree, (int, float)):
        return tree

    if isinstance(tree, tuple):
        if tree[0] == 'neg':
            return -evaluate_tree(tree[1])

        op, left, right = tree
        lv = evaluate_tree(left)
        rv = evaluate_tree(right)

        if op == '+':
            return lv + rv
        if op == '-':
            return lv - rv
        if op == '*':
            return lv * rv
        if op == '/':
            if rv == 0:
                raise ZeroDivisionError("Division by zero")
            return lv / rv

    raise ValueError(f"Unknown tree node: {tree}")


def format_result(value):
    """Format numeric result: integer if whole, else 4 decimal places."""
    if value == int(value):
        return str(int(value))
    return str(round(value, 4))




def evaluate_file(input_path: str) -> list:
    """
    Reads expressions from input_path (one per line).
    Writes output.txt to the same directory.
    Returns a list of dicts: {input, tree, tokens, result}
    """
    output_dir = os.path.dirname(os.path.abspath(input_path))
    output_path = os.path.join(output_dir, "output.txt")

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    results = []
    output_blocks = []

    for line in lines:
        expr = line.strip()
        if not expr:
            continue

        entry = {'input': expr, 'tree': 'ERROR', 'tokens': 'ERROR', 'result': 'ERROR'}

        
        tokens = tokenise(expr)

        if tokens is None:
           
            output_blocks.append(
                f"Input: {expr}\n"
                f"Tree: ERROR\n"
                f"Tokens: ERROR\n"
                f"Result: ERROR"
            )
            results.append(entry)
            continue

        token_str = format_tokens(tokens)

        
        try:
            tree = parse(list(tokens)) 
            tree_str = tree_to_str(tree)
        except ParseError:
            output_blocks.append(
                f"Input: {expr}\n"
                f"Tree: ERROR\n"
                f"Tokens: ERROR\n"
                f"Result: ERROR"
            )
            results.append(entry)
            continue

        
        try:
            value = evaluate_tree(tree)
            result_str = format_result(value)
            entry = {
                'input': expr,
                'tree': tree_str,
                'tokens': token_str,
                'result': value   # float as per spec
            }
            output_blocks.append(
                f"Input: {expr}\n"
                f"Tree: {tree_str}\n"
                f"Tokens: {token_str}\n"
                f"Result: {result_str}"
            )
        except (ZeroDivisionError, ValueError):
            entry = {
                'input': expr,
                'tree': tree_str,
                'tokens': token_str,
                'result': 'ERROR'
            }
            output_blocks.append(
                f"Input: {expr}\n"
                f"Tree: {tree_str}\n"
                f"Tokens: {token_str}\n"
                f"Result: ERROR"
            )

        results.append(entry)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(output_blocks) + '\n')

    print(f"[✓] Output written to '{output_path}'")
    return results



if __name__ == "__main__":
    import sys

    print("=" * 50)
    print("  HIT137 Assignment 2 - Question 2")
    print("  Mathematical Expression Evaluator")
    print("=" * 50)

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("\nEnter path to input file (default: sample_input.txt): ").strip()
        if not path:
            path = "sample_input.txt"

    if not os.path.exists(path):
        print(f"Error: File '{path}' not found.")
        sys.exit(1)

    results = evaluate_file(path)

    print(f"\nProcessed {len(results)} expression(s).\n")
    for r in results:
        print(f"  {r['input']}  →  {r['result']}")

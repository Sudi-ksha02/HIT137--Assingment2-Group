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
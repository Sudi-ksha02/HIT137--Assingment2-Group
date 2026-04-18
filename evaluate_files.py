def evaluate_file(input_path: str) -> list:
   
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

        # ── Tokenise ──────────────────────────────────
        tokens = tokenise(expr)

        if tokens is None:
            # Invalid character found
            output_blocks.append(
                f"Input: {expr}\n"
                f"Tree: ERROR\n"
                f"Tokens: ERROR\n"
                f"Result: ERROR"
            )
            results.append(entry)
            continue

        token_str = format_tokens(tokens)

        # ── Parse ─────────────────────────────────────
        try:
            tree = parse(list(tokens))  # pass a copy
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

        # ── Evaluate ──────────────────────────────────
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

    # Write output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(output_blocks) + '\n')

    print(f"[✓] Output written to '{output_path}'")
    return results
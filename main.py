if _name_ == "_main_":
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
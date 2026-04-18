def verify_decryption(original_path, decrypted_path):
    """
    Compare raw_text.txt with decrypted_text.txt.
    Print whether decryption was successful and return True/False.
    """
    with open(original_path, 'r', encoding='utf-8') as f:
        original  = f.read()
    with open(decrypted_path, 'r', encoding='utf-8') as f:
        decrypted = f.read()

    if original == decrypted:
        print("[+] Verification PASSED: Decrypted text matches the original exactly.")
        return True
    else:
        print("[-] Verification FAILED: Decrypted text does NOT match the original.")
        for i, (a, b) in enumerate(zip(original, decrypted)):
            if a != b:
                print(f"    First mismatch at index {i}: original={repr(a)}, decrypted={repr(b)}")
                break
        return False

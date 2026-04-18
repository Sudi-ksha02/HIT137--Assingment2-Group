
def encrypt_char(ch, shift1, shift2):
    """Return the encrypted version of a single character."""
    if ch.islower():
        base = ord('a')
        idx  = ord(ch) - base
        new_idx = (idx + shift1 * shift2) % 26 if idx <= 12 else (idx - (shift1 + shift2)) % 26
        return chr(base + new_idx)
    elif ch.isupper():
        base = ord('A')
        idx  = ord(ch) - base
        new_idx = (idx - shift1) % 26 if idx <= 12 else (idx + shift2 ** 2) % 26
        return chr(base + new_idx)
    return ch  # space, digit, punctuation unchanged


def decrypt_char(ch, shift1, shift2):
    """
    Return the decrypted version of a single character.
    Reverses the encryption rule based on the encrypted character's half-range.
    """
    if ch.islower():
        base = ord('a')
        idx  = ord(ch) - base
        new_idx = (idx - shift1 * shift2) % 26 if idx <= 12 else (idx + (shift1 + shift2)) % 26
        return chr(base + new_idx)
    elif ch.isupper():
        base = ord('A')
        idx  = ord(ch) - base
        new_idx = (idx + shift1) % 26 if idx <= 12 else (idx - shift2 ** 2) % 26
        return chr(base + new_idx)
    return ch


def encrypt_file(input_path, output_path, shift1, shift2):
    """Read plain text from input_path, encrypt, and write to output_path."""
    with open(input_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    encrypted_text = ''.join(encrypt_char(ch, shift1, shift2) for ch in raw_text)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)
    print(f"[+] Encrypted text written to '{output_path}'")
    return encrypted_text


def decrypt_file(input_path, output_path, shift1, shift2):
    """Read encrypted text from input_path, decrypt, and write to output_path."""
    with open(input_path, 'r', encoding='utf-8') as f:
        encrypted_text = f.read()
    decrypted_text = ''.join(decrypt_char(ch, shift1, shift2) for ch in encrypted_text)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)
    print(f"[+] Decrypted text written to '{output_path}'")
    return decrypted_text


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


def main():
    print("=" * 55)
    print("  HIT137 Assignment 2  -  Question 1")
    print("  Text Encryption / Decryption Program")
    print("=" * 55)

    # Step 1: Prompt the user for shift values
    while True:
        try:
            shift1 = int(input("\nEnter shift1 (positive integer): ").strip())
            shift2 = int(input("Enter shift2 (positive integer): ").strip())
            if shift1 <= 0 or shift2 <= 0:
                print("  Both values must be positive integers. Try again.")
                continue
            break
        except ValueError:
            print("  Invalid input. Please enter whole numbers.")

    print(f"\n  shift1={shift1}, shift2={shift2}")
    print(f"  Lowercase a-m: +{shift1 * shift2}  |  n-z: -{shift1 + shift2}")
    print(f"  Uppercase A-M: -{shift1}            |  N-Z: +{shift2 ** 2}")
    print()

    raw_path       = "raw_text.txt"
    encrypted_path = "encrypted_text.txt"
    decrypted_path = "decrypted_text.txt"

    # Step 2: Encrypt
    encrypt_file(raw_path, encrypted_path, shift1, shift2)

    # Step 3: Decrypt
    decrypt_file(encrypted_path, decrypted_path, shift1, shift2)

    # Step 4: Verify
    verify_decryption(raw_path, decrypted_path)

    print("\nDone.")


if __name__ == "__main__":
    main()

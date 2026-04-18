def encrypt_file(input_path, output_path, shift1, shift2):
    """Read plain text from input_path, encrypt, and write to output_path."""
    with open(input_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    encrypted_text = ''.join(encrypt_char(ch, shift1, shift2) for ch in raw_text)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)
    print(f"[+] Encrypted text written to '{output_path}'")
    return encrypted_text
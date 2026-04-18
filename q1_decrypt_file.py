def decrypt_file(input_path, output_path, shift1, shift2):
    """Read encrypted text from input_path, decrypt, and write to output_path."""
    with open(input_path, 'r', encoding='utf-8') as f:
        encrypted_text = f.read()
    decrypted_text = ''.join(decrypt_char(ch, shift1, shift2) for ch in encrypted_text)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)
    print(f"[+] Decrypted text written to '{output_path}'")
    return decrypted_text
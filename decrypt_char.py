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
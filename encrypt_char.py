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
    return ch 

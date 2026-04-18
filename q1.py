# HIT137 Assignment 2 - Question 1
# Encryption and Decryption Program
#
# Concepts used (all from class slides):
#   - Functions with parameters and return values  (Week 4)
#   - ord() and chr() for ASCII conversion         (Week 3)
#   - String methods: islower(), isupper()         (Week 3)
#   - if / else control flow                       (Week 2)
#   - Modulo operator % for wrap-around            (Week 2)
#   - for loop to iterate over characters          (Week 2)
#   - Reading and writing text files               (Week 3)
#   - String concatenation and comparison          (Week 3)
#
# Encryption Rules:
#   Lowercase a-m  : shift FORWARD  by shift1 * shift2  (mod 26)
#   Lowercase n-z  : shift BACKWARD by shift1 + shift2  (mod 26)
#   Uppercase A-M  : shift BACKWARD by shift1           (mod 26)
#   Uppercase N-Z  : shift FORWARD  by shift2 squared   (mod 26)
#   Other chars    : unchanged (spaces, numbers, symbols)


# ----------------------------------------------------------
# ENCRYPT a single character
# ----------------------------------------------------------
def encrypt_char(ch, shift1, shift2):
    if ch.islower():
        base = ord('a')
        index = ord(ch) - base
        if index <= 12:                          # letters a to m
            new_index = (index + shift1 * shift2) % 26
        else:                                    # letters n to z
            new_index = (index - (shift1 + shift2)) % 26
        return chr(base + new_index)

    elif ch.isupper():
        base = ord('A')
        index = ord(ch) - base
        if index <= 12:                          # letters A to M
            new_index = (index - shift1) % 26
        else:                                    # letters N to Z
            new_index = (index + shift2 ** 2) % 26
        return chr(base + new_index)

    else:
        return ch                                # space, digit, punctuation — no change


# ----------------------------------------------------------
# DECRYPT a single character  (reverse of encrypt)
# ----------------------------------------------------------
def decrypt_char(ch, shift1, shift2):
    if ch.islower():
        base = ord('a')
        index = ord(ch) - base
        if index <= 12:                          # reverse of a-m rule
            new_index = (index - shift1 * shift2) % 26
        else:                                    # reverse of n-z rule
            new_index = (index + (shift1 + shift2)) % 26
        return chr(base + new_index)

    elif ch.isupper():
        base = ord('A')
        index = ord(ch) - base
        if index <= 12:                          # reverse of A-M rule
            new_index = (index + shift1) % 26
        else:                                    # reverse of N-Z rule
            new_index = (index - shift2 ** 2) % 26
        return chr(base + new_index)

    else:
        return ch


# ----------------------------------------------------------
# ENCRYPT FILE
# Reads raw_text.txt, encrypts every character,
# writes result to encrypted_text.txt
# ----------------------------------------------------------
def encrypt_file(input_path, output_path, shift1, shift2):
    input_file = open(input_path, 'r')
    raw_text = input_file.read()
    input_file.close()

    encrypted_text = ""
    for ch in raw_text:
        encrypted_text = encrypted_text + encrypt_char(ch, shift1, shift2)

    output_file = open(output_path, 'w')
    output_file.write(encrypted_text)
    output_file.close()

    print("Encrypted text written to: " + output_path)


# ----------------------------------------------------------
# DECRYPT FILE
# Reads encrypted_text.txt, decrypts every character,
# writes result to decrypted_text.txt
# ----------------------------------------------------------
def decrypt_file(input_path, output_path, shift1, shift2):
    input_file = open(input_path, 'r')
    encrypted_text = input_file.read()
    input_file.close()

    decrypted_text = ""
    for ch in encrypted_text:
        decrypted_text = decrypted_text + decrypt_char(ch, shift1, shift2)

    output_file = open(output_path, 'w')
    output_file.write(decrypted_text)
    output_file.close()

    print("Decrypted text written to: " + output_path)


# ----------------------------------------------------------
# VERIFY DECRYPTION
# Compares raw_text.txt with decrypted_text.txt
# Prints whether they match or not
# ----------------------------------------------------------
def verify_decryption(original_path, decrypted_path):
    original_file = open(original_path, 'r')
    original_text = original_file.read()
    original_file.close()

    decrypted_file = open(decrypted_path, 'r')
    decrypted_text = decrypted_file.read()
    decrypted_file.close()

    if original_text == decrypted_text:
        print("Verification PASSED: Decrypted text matches the original.")
    else:
        print("Verification FAILED: Decrypted text does not match the original.")


# ----------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------
def main():
    print("HIT137 Assignment 2 - Question 1")
    print("Text Encryption and Decryption")
    print("----------------------------------")

    # Step 1: Get shift values from user
    shift1 = int(input("Enter shift1 (positive integer): "))
    shift2 = int(input("Enter shift2 (positive integer): "))

    print("")
    print("shift1 = " + str(shift1) + ", shift2 = " + str(shift2))
    print("Lowercase a-m shift: +" + str(shift1 * shift2))
    print("Lowercase n-z shift: -" + str(shift1 + shift2))
    print("Uppercase A-M shift: -" + str(shift1))
    print("Uppercase N-Z shift: +" + str(shift2 ** 2))
    print("")

    # File names
    raw_path       = "raw_text.txt"
    encrypted_path = "encrypted_text.txt"
    decrypted_path = "decrypted_text.txt"

    # Step 2: Encrypt the file
    encrypt_file(raw_path, encrypted_path, shift1, shift2)

    # Step 3: Decrypt the file
    decrypt_file(encrypted_path, decrypted_path, shift1, shift2)

    # Step 4: Verify decryption
    verify_decryption(raw_path, decrypted_path)

    print("")
    print("Done.")


main()

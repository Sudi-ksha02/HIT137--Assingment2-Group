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
    if _name_ == "_main_":
    main()

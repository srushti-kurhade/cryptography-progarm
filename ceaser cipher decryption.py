def decrypt_caesar(ciphertext, shift):
    result = ""

    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(start + (ord(char) - start - shift_amount) % 26)
            result += decrypted_char
        else:
            result += char

    return result


def main():
    shift = int(input("Enter the shift value (an integer): "))

    # Get the ciphertext (encrypted message) from the user
    ciphertext = input("Enter the encrypted message: ")

    # Decrypt the message
    print("Decrypted message:", decrypt_caesar(ciphertext, shift))


if __name__ == "__main__":
    main()

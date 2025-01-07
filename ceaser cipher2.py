def encrypt_caesar(plaintext, shift):
    result = ""

    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            result += encrypted_char
        else:
            result += char

    return result


def main():
    print("Welcome to the Caesar Cipher Encryption Program!")

    # Get the shift value from the user
    shift = int(input("Enter the shift value (an integer): "))

    # Get the message from the user
    message = input("Enter the message: ")

    # Encrypt the message
    print("Encrypted message:", encrypt_caesar(message, shift))


if __name__ == "__main__":
    main()

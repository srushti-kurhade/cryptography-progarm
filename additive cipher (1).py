def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = (ord(char.upper()) - 65 + key) % 26
            cipher_char = chr(shift + 65)
            ciphertext += cipher_char
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = (ord(char.upper()) - 65 - key) % 26
            plain_char = chr(shift + 65)
            plaintext += plain_char
        else:
            plaintext += char
    return plaintext


def main():
    text = input("Enter the text: ")
    key = int(input("Enter the key: "))

    encrypted = encrypt(text, key)
    print(f"Encrypted Text: {encrypted}")

    decrypted = decrypt(encrypted, key)
    print(f"Decrypted Text: {decrypted}")


if __name__ == "__main__":
    main()

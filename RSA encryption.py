# Function to compute the modular inverse
def mod_inverse(e, phi):
    k = 1
    while (k * phi + 1) % e != 0:
        k += 1
    return (k * phi + 1) // e

# Function to generate RSA keys
def generate_rsa_keys():
    p = int(input("enter first prime number:  ")) # First prime number
    q = int(input("enter second prime number:  "))  # Second prime number
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 5  # Public exponent
    d = mod_inverse(e, phi)  # Private exponent
    return (n, e), (n, d)  # Public key and private key

# Function to decrypt a message
def decrypt(private_key, ciphertext):
    n, d = private_key
    return pow(ciphertext, d, n)

# Example usage
_, private_key = generate_rsa_keys()

# Assume we already have the ciphertext from the encryption program
ciphertext =11 # Replace with the actual encrypted value
decrypted_message = decrypt(private_key, ciphertext)
print("Decrypted message (M) =", decrypted_message)
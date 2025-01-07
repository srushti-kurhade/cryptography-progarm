# Function to find the greatest common divisor of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute the modular inverse
def mod_inverse(e, phi):
    k = 1
    while (k * phi + 1) % e != 0:
        k += 1
    return (k * phi + 1) // e

# Function to generate RSA keys
def generate_rsa_keys():
    p = int(input("enter first prime number:  "))# First prime number
    q = int(input("enter second prime number:  "))  # Second prime number
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 7  # Public exponent
    d = mod_inverse(e, phi)  # Private exponent
    return (n, e), (n, d)  # Public key and private key

# Function to encrypt a message
def encrypt(public_key, message):
    n, e = public_key
    return pow(message, e, n)

# Example usage
public_key, _ = generate_rsa_keys()

# Encrypt a message
message =11  # Example message (must be a number less than n)
ciphertext = encrypt(public_key, message)
print("Encrypted message (C) =", ciphertext)


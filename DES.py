# DES Algorithm Implementation
def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)


def left_shift(bits, n):
    return bits[n:] + bits[:n]


def generate_keys(key):
    # Key permutation table
    key_permutation = [57, 49, 41, 33, 25, 17, 9, 1,
                       58, 50, 42, 34, 26, 18, 10, 2,
                       59, 51, 43, 35, 27, 19, 11, 3,
                       60, 52, 44, 36, 63, 55, 47, 39,
                       31, 23, 15, 7, 62, 54, 46, 38,
                       30, 22, 14, 6, 61, 53, 45, 37,
                       29, 21, 13, 5, 28, 20, 12, 4]

    # Key compression table
    key_compression = [14, 17, 11, 24, 1, 5, 3, 28,
                       15, 6, 21, 10, 23, 19, 12, 4,
                       26, 8, 16, 7, 27, 20, 13, 2,
                       41, 52, 31, 37, 47, 55, 30, 40,
                       51, 45, 33, 48, 44, 49, 39, 56,
                       34, 24, 29, 39, 8, 11, 30, 18,
                       42, 26, 1, 2, 35, 38, 20, 6]

    # Split into two halves
    key = permute(key, key_permutation)
    left, right = key[:28], key[28:]

    # Number of shifts
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    keys = []

    for shift in shifts:
        left = left_shift(left, shift)
        right = left_shift(right, shift)
        combined = left + right
        keys.append(permute(combined, key_compression))

    return keys


# S-boxes for DES
S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 2, 8, 14, 3, 10, 6, 12, 4, 9, 1, 7, 5, 11, 0, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 2, 8, 4, 7, 6, 12],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 15, 11, 12, 1],
        [13, 6, 4, 9, 8, 1, 0, 15, 7, 10, 14, 3, 11, 2, 5, 12],
        [2, 8, 12, 1, 10, 14, 7, 4, 6, 9, 0, 15, 13, 3, 5, 11]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 2, 8, 5, 12, 4, 11, 15, 1],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        [2, 8, 12, 1, 10, 14, 7, 4, 6, 9, 0, 15, 13, 3, 5, 11],
        [0, 1, 14, 7, 6, 10, 2, 9, 11, 13, 8, 5, 4, 12, 3, 15]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 14, 1, 7, 6, 0, 8, 11, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 10, 2, 8, 3, 11, 4, 7, 5, 14, 1, 9, 12, 0, 15, 13]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 4, 9, 7, 2, 8, 14, 12, 0, 6, 11, 3, 5, 10],
        [6, 5, 9, 10, 0, 12, 2, 8, 4, 11, 15, 1, 3, 14, 7, 13],
        [4, 11, 10, 13, 0, 14, 8, 7, 9, 12, 15, 1, 2, 3, 6, 5]
    ]
]


def s_box_lookup(bits):
    row = int(bits[0] + bits[5], 2)  # First and last bits
    col = int(bits[1:5], 2)  # Middle bits
    return format(S_BOXES[row][col], '04b')


def feistel_function(right, subkey):
    # Expansion permutation
    expansion_table = [32, 1, 2, 3, 4, 5, 4, 5,
                       6, 7, 8, 9, 8, 9, 10, 11,
                       12, 13, 14, 15, 16, 17, 16, 17,
                       18, 19, 20, 21, 20, 21, 22, 23,
                       24, 25, 26, 27, 28, 29, 28, 29,
                       30, 31, 32, 1]

    # Apply expansion permutation
    expanded_right = permute(right, expansion_table)

    # XOR with subkey
    xored = format(int(expanded_right, 2) ^ int(subkey, 2), '048b')

    # S-box substitution
    substituted = ''
    for i in range(0, 48, 6):
        block = xored[i:i + 6]
        substituted += s_box_lookup(block)

    # Permutation
    p_table = [16, 7, 20, 21, 29, 12, 28, 17,
               1, 15, 23, 26, 5, 18, 31, 10,
               2, 8, 24, 14, 32, 27, 3, 9,
               19, 13, 30, 6, 22, 11, 4, 25]
    return permute(substituted, p_table)


def des_encrypt(plaintext, key):
    # Initial permutation
    initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                           60, 52, 44, 36, 28, 20, 12, 4,
                           62, 54, 46, 38, 30, 22, 14, 6,
                           64, 56, 48, 40, 32, 24, 16, 8]

    # Final permutation
    final_permutation = [40, 8, 48, 16, 56, 24, 32, 0,
                         30, 62, 1, 43, 6, 58, 33, 17,
                         7, 39, 26, 54, 12, 36, 46, 2,
                         50, 14, 27, 42, 5, 59, 34, 22,
                         9, 63, 19, 12, 28, 48, 15, 37,
                         8, 11, 41, 44, 31, 4, 24, 53,
                         29, 3, 13, 26, 23, 20, 2, 45]

    keys = generate_keys(key)

    # Apply initial permutation
    bits = permute(plaintext, initial_permutation)
    left, right = bits[:32], bits[32:]

    # 16 rounds of processing
    for i in range(16):
        new_right = format(int(left, 2) ^ int(feistel_function(right, keys[i]), 2), '032b')
        left, right = right, new_right

    # Combine left and right and apply final permutation
    combined = right + left
    ciphertext = permute(combined, final_permutation)

    return ciphertext


def des_decrypt(ciphertext, key):
    keys = generate_keys(key)[::-1]  # Reverse the keys for decryption
    return des_encrypt(ciphertext, keys)


# Example usage
if __name__ == "__main__":
    key = "1010101010101010"  # Example key (64 bits, 8 bytes)
    plaintext = "ABCDEFGH"  # Example plaintext (must be 64 bits)

    # Convert plaintext to binary string (8 bytes)
    plaintext_bin = ''.join(format(ord(char), '08b') for char in plaintext)

    # Encrypt the plaintext
    ciphertext = des_encrypt(plaintext_bin, key)
    print("Ciphertext:", ciphertext)

    # Decrypt the ciphertext
    decrypted_text = des_decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)

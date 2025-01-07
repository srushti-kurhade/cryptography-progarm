def diffie_hellman():
    q = 23
    alpha = 5


    X_a = 6
    X_b = 15

    Y_a = (alpha ** X_a) % q
    Y_b = (alpha ** X_b) % q

    print("Alice's public key:", Y_a)
    print("Bob's public key:", Y_b)


    shared_secret_A = (Y_b ** X_a) % q
    shared_secret_B = (Y_a ** X_b) % q

    print("Shared secret (Alice):", shared_secret_A)
    print("Shared secret (Bob):", shared_secret_B)

    if shared_secret_A == shared_secret_B:
        print("Diffie-Hellman secret keys can be exchanged.")
    else:
        print("Diffie-Hellman secret keys cannot be exchanged.")

# Run the Diffie-Hellman key exchange
diffie_hellman()

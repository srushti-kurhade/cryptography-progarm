def encrypt_caeser(plaintext,shift):
    result=""

    for char in plaintext:
        if char.isalpha():
            shift_amount=shift%26
            start=ord('A') if char.isupper() else ord('a')
            encrypted_char=chr(start+(ord(char)-start+shift_amount)%26)
            result+=  encrypted_char
        else:
            result+=char
    return result
def decrypt_caeser(ciphertext,shift):
    return encrypt_ceaser(ciphertext,-shift)

def main():
    print("Welcome to the Ceaser Cipher program!")
    choice=input("Would you like to (e)ncrypt or (d)ecrypt?").lower()
    if choice not in ['e','d']:
        print("Invalid choice.Please select 'e' for encryption or 'd' for decryption")
        return
    while True:
        try:
            shift=int(input("enter the shift value(an integer):"))
            break
        except ValueError:
            print("Invalid input.Please enter an integer for the shift value.")
    message=input("Enter the message:")
    if choice=='e':
        encrypted_message=encrypt_caeser(message,shift)
        print(f"Encrypted message:{encrypted_message}")
    elif choice=='d':
        decrypted_message=decrypt_caeser(message,shift)
        print(f"Decrypted Message:{decrypted_message}"
if __name__=="__main__":
   main()



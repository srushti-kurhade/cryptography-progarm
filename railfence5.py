def railfence_encrypt(text,rails):

    if rails < 2:
        return text

    rails_down =True
    current_rail = 0
    result = [""]*rails

    for char in text:
        result[current_rail]+=char
        if current_rail == rails -1:
            rails_down = False
        elif current_rail ==0:
            rails_down = True

        current_rail+= 1 if rails_down else -1

    return "".join(result)
text=input("Enter a plaintext: ")
rails =int(input("Enter the number of rails: "))

encrypted_text=railfence_encrypt(text,rails)
print("Encrypted text: ",encrypted_text)


def singlecolumnar(p, key_length):
    col=[''] * key_length
    for i,char in enumerate(p):
        col[i % key_length] += char
    return ''.join(col)


msg = input("Enter the msg: ")
key1= input("Enter the  first key: ")

encrypted_msg=singlecolumnar(msg,len(key1))
print("Encrypted message: ",encrypted_msg)
import math

key= str(input("Enter key: "))
def encryption(msg):
    msg= msg.replace(" ","_")
    cipher=""

    col = len(key)
    row = int(math.ceil(len(msg)/col))

    null_val = (row*col) - len(msg)
    msg +='_'*null_val
    matrix=[]

    for i in range(0,len(msg),col):
        matrix.append(msg[i:i+col])

    key_1st=sorted(list(key))

    for k in key_1st:
        curr_ind=key.index(k)
        cipher += ''.join(row[curr_ind] for row in matrix)

    return cipher

if __name__ == "__main__" :
    msg=input("Enter plaintext: ")
    cipher = encryption(msg)
    print("Encryption Message: ", cipher)

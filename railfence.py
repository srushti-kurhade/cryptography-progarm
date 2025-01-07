def rail_fence(p,key):
    rail=['']*key
    row=0
    direction=1
    for char in p:
        rail[row]+=char
        row+=direction

        if row==0 or row==key-1:
            direction*=-1
    return ' '.join(rail)
msg=input("Enter the msg: ")
key=int(input("Enter the key: "))
final=rail_fence(msg,key)
print(f"Output: {final}")

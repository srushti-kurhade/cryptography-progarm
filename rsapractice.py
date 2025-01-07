def RSA():
    p=int(input("Enter the value of p: "))
    q=int(input("Enter the value of q: "))
    n = p*q
    print("n :" ,n)
    phi=(p-1) *(q-1)
    print("phi: " ,phi)
    e=5
    print("e: " ,e)
    k=1
    while 1+k*phi%e!=0:
        k=k+1
    d=1+k*phi//e
    print("d: ",d)
    M=10
    C=pow(M,e,n)
    print("C: ",C)
    M=pow(C,d,n)
    print("M :", M)
RSA()

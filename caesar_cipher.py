choice=int(input("Enter choice : 1.Encryption 2.Decryption:"))
if choice==1:
    pt=input("Enter plain text : ")
    k=int(input("Enter key value : "))
    ct=""
    for i in range(len(pt)):
        ch=pt[i]
        if ch.isupper():
            ct = ct + chr(((ord(ch) + k - 65) % 26) + 65)
        else:
            ct = ct + chr(((ord(ch) + k - 97) % 26) + 97)
    print("Cipher text is : ",ct)
elif choice==2:
    ct=input("Enter cipher text : ")
    k=int(input("Enter key value : "))
    pt=""
    for i in range(len(ct)):
        ch=ct[i]
        if ch.isupper():
            pt = pt + chr(((ord(ch) - k - 65) % 26) + 65)
        else:
            pt = pt + chr(((ord(ch) - k - 97) % 26) + 97)
    print("Plain text is : ",pt)

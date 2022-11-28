def bruteForce(ct): 
    for k in range(1,27):
        pt="" 
        for a in ct:
            if(ord(a)>=65 and ord(a)<=90): 
                pt+=chr((ord(a)-65-k)%26+65) 
            if(ord(a)>=97 and ord(a)<=122): 
                pt+=chr((ord(a)-97-k)%26+97) 
        print(pt) 
pt = input("Enter the text: ") 
ct="" 
k=int(input("Enter the key: ")) 
#at sender's side 
for a in pt:
    if(ord(a)>=65 and ord(a)<=90):
        ct+=chr((ord(a)-65+k)%26+65) 
    if(ord(a)>=97 and ord(a)<=122): 
        ct+=chr((ord(a)-97+k)%26+97) 
print("Cypher text: ",ct) 
#at receiver's side 
dt="" 
for a in ct:
    if(ord(a)>=65 and ord(a)<=90):
        dt+=chr((ord(a)-65-k)%26+65) 
    if(ord(a)>=97 and ord(a)<=122): 
        dt+=chr((ord(a)-97-k)%26+97) 
print("Plain text: ",dt) 
bruteForce(ct)

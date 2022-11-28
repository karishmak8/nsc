m=input("enter message: ")
m_list=[]
for c in m:
    m_list.append(ord(c)-65)

p=int(input("enter 1st prime no: "))
q=int(input("enter 2nd prime no: "))
n=p*q
fxn=(p-1)*(q-1)

for e in range(2,fxn):
    c=0
    for j in range(2,e+1):
        if(e%j==0 and fxn%j==0):
            c=1        
    if c==0:
        break 
print("public key",e)

for d in range(1,fxn):
    if(d*e%fxn==1): 
        break 

print("private key",d)
#encryption
cipher=[]
for m in m_list:
    cipher.append((m**e)%n)
print("cipher-text number list",cipher)
c_text = ''
for i in cipher:
    c_text += chr((i+65)) 
print("Ciphered text: ",c_text)
# print("cipher text is",ct)
#decryption
msg=[]
for c in cipher:
    msg.append((c**d)%n)
dec=""
for i in msg:
    dec+=chr(i+65)

print("message delivered",dec) 

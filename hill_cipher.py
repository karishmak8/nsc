km = [[0]*3 for i in range(3)]
mv = [[0]*3 for i in range(3)]
cm = [[0]*3 for i in range(3)]
cc = [[0]*3 for i in range(3)]
de = [[0]*3 for i in range(3)]
b = [[0]*3 for i in range(3)]
def getKeyMatrix(key):
    k=0
    for i in range(3):
        for j in range(3):
            km[i][j] = ord(key[k]) % 65
            k=k+1
def encrypt(mv):
    for i in range(3):
        for j in range(3):
            cm[i][j]=0
            for x in range(3):
                cm[i][j] += (km[i][x] * mv[x][j])
            cc[i][j] = cm[i][j]
            cm[i][j] = cm[i][j] % 26
    ct=[]
    for i in range(3):
        ct.append(chr(cm[i][0] + 65))
    print("Encrypted Ciphertext : ","".join(ct))
'''def inversematrix():
    for i in range(3):
        for j in range(3):
            if(i == j):
                b[i][j]=1
            else:
                b[i][j]=0
    for k in range(3):
        for i in range(3):
            p = km[i][k]
            q = km[k][k]
            for j in range(3):
                if(i != k):
                    km[i][j] = (km[i][j]*q) - (p*km[k][j])
                    b[i][j] = (b[i][j]*q) - (p*b[k][j])
    for i in range(3):
        for j in range(3):
            b[i][j] = b[i][j] / km[i][i]'''
def inversematrix():
    det=0
    for i in range(3):
        det=det+(km[0][i] * (km[1][(i+1)%3] * km[2][(i+2)%3] - km[1][(i+2)%3] * km[2][(i+1)%3]));
    for i in range(3):
        for j in range(3):
            b[i][j]=(((km[(j+1)%3][(i+1)%3] * km[(j+2)%3][(i+2)%3]) - (km[(j+1)%3][(i+2)%3] * km[(j+2)%3][(i+1)%3]))/ det)
def decrypt():
    inversematrix()
    for i in range(3):
        for j in range(3):
            for k in range(3):
                de[i][j] = de[i][j] + int(b[i][k] * cc[k][j])
    d=[]
    for i in range(3):
        d.append(chr(((de[i][0])%26)+65))
    print("Decrypted Plaintext : ","".join(d))
def hillcipher(m,key):
    getKeyMatrix(key)
    for i in range(3):
        mv[i][0] = ord(m[i]) % 65
    encrypt(mv)
    decrypt()
 
m=input("Enter plain text : ")
key=input("Enter the key : ")
hillcipher(m,key)

#key=RJSHJMTJK


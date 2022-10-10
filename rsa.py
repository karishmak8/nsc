def gcd(a,b):
    while(a>0):
        c=b%a
        b=a
        a=c
    return b
p=int(input("enter 1st prime:"))
q=int(input("enter 2nd prime:"))
m=int(input("enter message:"))
n=p*q
fn=(p-1)*(q-1)
for i in range(2,fn):
    if(gcd(i,fn)==1):
        e=i
        break
i=0
while(True):
    if((i*e)%fn==1):
        d=i
        break
    i+=1
c=(pow(m,e))%n
print("encrypted msg:"+str(c))
m1=(pow(c,d))%n
print("decrypted msg:"+str(m1))

#11
#5
#8

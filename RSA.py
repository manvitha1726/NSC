m=int(input("enter message: "))
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
cipher=(m**e)%n 
print("cipher-text is",cipher)
#decryption
msg=(cipher**d)%n 
print("message delivered",msg) 

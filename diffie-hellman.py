q=int(input("Enter any prime number: "))
for alpha in range(1,q):
    s=[]
    for x in range(0,q-1): 
        s.append(alpha**x%q) 
    if(len(s)==len(set(s))):
        break 
print("alpha value is",alpha)
Xa=int(input("Enter private Xa :"))
Ya=alpha**Xa%q 
print("public key Ya :",Ya)
Xb=int(input("Enter private Xb :"))
Yb=alpha**Xb%q  
print("public key Yb :",Yb)

Ka=Yb**Xa%q 
Kb=Ya**Xb%q 
print("ka,kb:",Ka,Kb)
if(Ka==Kb):
    print("Key can be shared")
else:
    print("Key can't be shared") 


#hill cipher encryption

import numpy as np

txt=input("Enter the plain text ")
key=input("Enter the key ")


txt_matrix=[]
for i in txt:
    if(i.isupper()):
        txt_matrix.append(ord(i)-65)
    else:
        txt_matrix.append(ord(i)-97)

key_matrix=[]
t=[]
for i in key:
    if(i.isupper()):
        t.append(ord(i)-65)
    else:
        t.append(ord(i)-97)

    if(len(t)==len(txt_matrix)):
        key_matrix.append(t)
        t=[]

txt_matrix=np.array(txt_matrix)
key_matrix=np.array(key_matrix)

res=np.dot(key_matrix,txt_matrix)
cipher=""
for i in res:
    cipher+=chr((i%26)+65)

print("The cipher text is",cipher)
n=5
import random
l=[]
used=[]
while True:
    x=random.randint(0,n)
    if x in used:
        continue
    else:
        l.append(x)
        used.append(x)
    if len(l)==5:
        break
print(l)

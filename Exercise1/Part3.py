#PART 2.1
#Fill arr with num if not in arr already
import random
n=5
l=[]
while True:
    x=random.randint(0,n)
    if x in l:
        continue
    else:
        l.append(x)
    if len(l)==5:
        break
print(l)

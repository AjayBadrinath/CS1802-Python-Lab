import random
n=5
l=[]
for i in range(n):
    l.append(i+1)
for i in range(n):
    index=random.randint(0,n-1)
    temp=l[i]
    l[i]=l[index]
    l[index]=temp
print(l)

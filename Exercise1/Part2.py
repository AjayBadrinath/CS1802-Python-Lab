#Part2. place first k element to sort in descending order then compare remaining k elements with others in the sorted array then swap places

def sort(seq,length):
    for _ in range(length):
        for j in range(_+1,length):
            if seq[_]<seq[j]:
                temp=seq[j]
                seq[j]=seq[_]
                seq[_]=temp
    for j in range(length):
        for i in range(length,len(seq)):
            if seq[j]<seq[i]:
                temp=seq[i]
                seq[i]=seq[j]
                seq[j]=temp
        
            
l=[22,1,3,44,53,23,54]
sort(l,5)
print(l)

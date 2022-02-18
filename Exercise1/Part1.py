#Find kth largest element in Group

#Part1.sort numbers in descending order and retrieve kth element
def sort(seq,len(seq)):
    for _ in range(len(seq)):
        for j in range(_+1,len(seq)):
            if seq[_]<seq[j]:
                temp=seq[j]
                seq[j]=seq[_]
                seq[_]=temp
l=[22,1,3,44,53,23,54]
sort(l,5)
print(l[0])


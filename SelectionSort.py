#selection sort
l=list(map(int,input("Enter the elements").split()))
n=len(l)
for i in range(n):
    minIndex=i
    for j in range(i+1,n):
        if(l[j]<l[minIndex]):
            minIndex=j
    l[minIndex],l[i]=l[i],l[minIndex]
print(l)

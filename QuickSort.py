def quicksort(a,low,high):
    if(low<high):
        p=partition(a,low,high)
        quicksort(a,low,p-1)
        quicksort(a,p+1,high)
def partition(a,low,high):
    pi=a[high]
    pIndex=low
    for i in range(low,high):
        if(a[i]<=pi):
            a[i],a[pIndex]=a[pIndex],a[i]
            pIndex+=1
    
    a[high],a[pIndex]=a[pIndex],a[high]
    return pIndex
l=list(map(int,input("Enter the elements").split()))
quicksort(l,0,len(l)-1)
print(l)

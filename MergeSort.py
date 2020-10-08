def mergesort(a):
    if(len(a)>1):
        m=len(a)//2
        L=a[:m]
        R=a[m:]
        mergesort(L)
        mergesort(R)
        i,j,k=0,0,0
        while(i<len(L) and j<len(R)):
            if(L[i]<R[j]):
                a[k]=L[i]
                i+=1
            else:
                a[k]=R[j]
                j+=1
            k+=1
        while(i<len(L)):
            a[k]=L[i]
            k+=1
            i+=1
        while(j<len(L)):
            a[k]=R[j]
            k+=1
            j+=1
a=list(map(int,input("Enter the elements").split()))
mergesort(a)
print(a)

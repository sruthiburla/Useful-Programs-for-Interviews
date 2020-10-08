l=list(map(int,input("Enter the Elements").split()))
n=len(l)
for i in range(1,n):
    temp=l[i]
    j=i-1
    while(j>=0 and temp<l[j]):
        l[j+1]=l[j]
        j-=1
    l[j+1]=temp
print(l)

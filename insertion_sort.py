a=[45,67,7,34,11,20,2]
n=7
for i in range (1,n):
    key = a[i]
    j=i-1
    while j>=0 and a[j] > key:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print(a) 
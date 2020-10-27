a=[45,67,7,34,11,20,2]
n=7
for i in range (0,n-1):
    indexofmin=i
    for j in range (i+1,n):
        if a[j] < a[indexofmin]:
            indexofmin = j
    #a[i],a[indexofmin]=a[indexofmin],a[i]
    temp=a[i]
    a[i]=a[indexofmin]
    a[indexofmin]=temp
print(a)

a=[45,7,34,11,20,2]
n=6
for i in range(0,n-1):
    for j in range (0,n-i-1): #we have taken n-i-1 because after evry pass last element is sorted so wo dont check that value in next pass.
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

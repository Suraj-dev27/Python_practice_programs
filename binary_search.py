pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        elif n > list[mid]:
            l = mid
        else:
            u = mid
list=[5,6,7,9,56,97,454]
n=454
if search(list,n):
    print(n,'Found at:',pos+1)
else:
    print('Not found!')
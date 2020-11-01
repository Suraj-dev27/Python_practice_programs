""" pos=-1
def search(lst,n):
    #i=0
    for i in range (len(lst)):
    #while i<len(lst):
        if lst[i]==n:
            globals()['pos']=i
            return True
        #i=i+1    this was defined for 'while loop', in for loop it is not required
    return False 
lst=[5,8,4,6,7,9,2]
n=7
if search(lst,n):
    print(n,"Found at position:",pos+1)
else:
    print("not found")
 """
#binary search practice
""" pos = -1
def bsearch(lst,n):
    
    low=0
    high=len(lst)
    while low < high:
        mid=(low+high)//2
        if n == lst[mid]:
            globals()['pos']=mid
            return True
        elif n > lst[mid]:
            low = mid
        else:
            high = mid
    return False
lst=[2,3,5,6,7,8,20,56]
n=20
if bsearch(lst,n):
    print(n,"is found at position:",pos+1)
else:
    print("not found") """


pos=-1
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
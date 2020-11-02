#find out pairs from array whose sum is same as given sum
def pair_sum(a,target):
    a.sort()
    left=0
    right=len(a)-1
    while(left<=right):
        if (a[left] + a[right]) > target:
            right=right-1
        elif (a[left]+a[right]) < target:
            left=left+1
        elif (a[left]+a[right])==target:
            print('sum of pair is:',a[left],'+',a[right],'=',target)
            left=left+1
            right=right-1


a=[3,4,8,5,6,10,7,19,9,21]
target=16
pair_sum(a,target)
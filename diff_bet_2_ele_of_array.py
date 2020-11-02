#minimum diff bet 2 elements of array

""" def minimu_diff_ele(arr):
    arr=sorted(arr)      #here it will take time complexity for sorting is: O(nlogn)
    n=len(arr)
    min_diff=9999*999
    for i in range(n-1):      #here it will take time complexity for looping is: O(n)         total time complexity is: T(n)=O(nlogn)
        if (arr[i+1]-arr[i] < min_diff):
            min_diff = arr[i+1]-arr[i]
    return min_diff


arr=[32,45,4,12,18,25]
print('Minimum diffrence between pair is:',minimu_diff_ele(arr)) """

#maximum diff bet 2 elements of array

def max_diff_ele(arr):
    arr=sorted(arr)
    max_diff=0
    for i in range (len(arr)-1):
        if arr[i+1]-arr[i] >max_diff:
            max_diff=arr[i+1]-arr[i]
    return max_diff

arr=[32,45,4,12,18,25]
print('Maximum difference between pair is:',max_diff_ele(arr))

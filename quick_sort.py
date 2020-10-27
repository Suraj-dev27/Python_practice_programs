def partition(a,low,high):
    i=(low-1)
    pivot=a[high]
    for j in range (low,high):
        if a[j]<=pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return(i+1)
def quick_sort(a,low,high):
    if low<high:
        pi=partition(a,low,high)
        quick_sort(a,low,pi-1)
        quick_sort(a,pi+1,high)
a=[2,5,3,8,6,5,4,7]
n=len(a)
quick_sort(a,0,n-1)
print("sorted array is:",a)

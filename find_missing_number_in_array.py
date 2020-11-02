def find_missing_num(a):
    n=a[-1]
    result=n*(n+1)//2   #here we have taken sum of n natural numbers
    sum1=sum(a)         #here we have taken sum of numbers in array
    print('missing number is:',result-sum1)


a=[1,2,3,5,6,7]
find_missing_num(a)

#we can also use XOR method
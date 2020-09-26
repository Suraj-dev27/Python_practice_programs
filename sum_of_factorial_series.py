#find sum of series sum=1!+2!+3!+4!+5!+.....+n!

'''n=int(input("Enter a number:"))
fact=1
a=1
sum=0
while (a<=n):
    fact *= a
    sum += fact
    a=a+1
print("sum of factorial is:", sum)'''

#find sum of series sum=1/1!+2/2!+3/3!+4/4!+5/5!+.....+n/n!

n=int(input("Enter a number:"))
fact=1
a=1
sum=0
while(a<=n):
    fact *= a
    sum += a/fact
    a += 1
print("sum of factorial is:", sum)
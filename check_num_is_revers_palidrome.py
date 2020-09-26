#reverse a number
'''n=int(input("Enter a number:"))
rev=0
num=n
while (n>0):
    rev=rev*10+(n%10)
    n=n//10
print("reverse of number",num,"is:",rev)'''

#check number is palindrome or not

'''n=int(input("Enter a number:"))
rev=0
num=n
while(n>0):
    rev=rev*10+(n%10)
    n=n//10
if num == rev:
    print("Number is palindrome!")
else:
    print("Number is not palindrome!")'''

#check string is palindrome or not

'''n=input("Enter a string:")
if n == n[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")'''

#check string is palindrome or not using function

def isPalindrome(n):
    return n == n[::-1]
n="madam"

ans=isPalindrome(n)
if ans:
    print("string is palindrome")
else:
    print("string is not palindrome")

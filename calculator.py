def addition(x,y):
    return x+y

def substraction(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def power(x,y):
    return pow(x,y)

print("Select one of following options")
print("1.Addition")
print("2.Substraction")
print("3.Multiply")
print("4.Divide")
print("5.Power")
choice=input("Select one number from(1/2/3/4/5): ")
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))

if choice=='1':
    print (num1,"+",num2,"=",addition(num1,num2))
elif choice=='2':
    print (num1,"-",num2,"=",substraction(num1,num2))
elif choice=='3':
    print (num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
    print (num1,"/",num2,"=",divide(num1,num2))
elif choice=='5':
    print (num1,"^",num2,"=",power(num1,num2))


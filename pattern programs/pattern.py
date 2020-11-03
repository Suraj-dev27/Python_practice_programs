# a=int(input("enter a number:"))
# for i in range(1,a):
#     print(" " * i, i,'\n')
# for j in range(a-2,0,-1):
#     print(" "*j,j,'\n')
a=int(input("enter number of lines:"))
for i in range (1,a):              # it is used to decide how many numbers to print.
    for j in range (1,i):                                               # it is used to print top left number.
        print(" ", end='')         # here all spaces before number are added and then on next line of code...
    print(" ",i, end='')           # here number is printed after spaces added by above line of code. 
    for l in range (88,2*i,-1):    # it is used to add middle distance between left pattern and right pattern.
        print(" ", end='')         # here spaces are added that specified by above line of code.
    for n in range(15,i,-1):       # it is used for top right space, it start from maximum space and then decease 1 by 1 for each number.
        print(" ", end='')         # it prints spaces defined by above line of code.
    print(i,end='')                                                      # it is used to print top right number.
    """ if i<10:                   
        print(" ", end='') """       
    """ for m in range (1,1):          
        print(" ",i, end='') """       
    print('\n')

for i in range (a,0,-1):         # it is used to decide how many numbers to print.
    for j in range (1,i):                                                 # it is used to print bottom left number.
        print(" ", end='')       # here all spaces before number are added and then on next line of code...
    print(" ",i, end='')         # here number is printed after spaces added by above line of code. 
    for l in range(90,2*i,-1):   # it is used to add middle distance between left pattern and right pattern.
        print(" ", end='')       # here spaces are added that specified by above line of code.
    for n in range(15,i,-1):     # it is used for bottom right space, it start from 1 and then increase space 1 by 1 for each number.
        print(" ", end='')       # it prints spaces defined by above line of code.
    print(i, end='')                                                       # it is used to print bottom right number.
    """ if i<10:
        print(" ", end='') 
    for m in range (1,1): """
    
    print('\n')


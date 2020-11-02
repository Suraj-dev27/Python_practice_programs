#finding common letters between 2 strings using &
def common_letter():
    str1=input("enter 1st string:")
    str2=input('enter 2nd string:')
    s1=set(str1)
    s2=set(str2)
    lst=s1&s2
    print(lst)
common_letter()
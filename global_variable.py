a=10
def something():
    a=9
    x=globals()['a'] # '=7' using this we can change the value of gloabal a from 10 to 7
    print('inside a:',a)
    print('outside a:',x)
something()
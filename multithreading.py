import time
import threading

square_result=[]
cube_result=[]

def square(arr):
    global square_result
    for num in arr:
        time.sleep(0.2)
        print('square:',num*num)
        square_result.append(num*num)
def cube(arr):
    global cube_result
    for num in arr:
        time.sleep(0.2)
        print('cube:',num*num*num)
        cube_result.append(num*num*num)

arr=[2,6,5,4]


t1=threading.Thread(target=square,args=(arr,))
t2=threading.Thread(target=cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
#square(arr)
#cube(arr)

print('square_result is:',sum(square_result))
print('cube_result is:',sum(cube_result))

t=time.time()
print('time taken:', time.time()-t)
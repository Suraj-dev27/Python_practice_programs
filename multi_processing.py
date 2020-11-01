import multiprocessing
import time

square_result=[]
cube_result=[]

def square (arr):
    global square_result
    for num in arr:
        time.sleep(0.2)
        print('square:',num*num)
        square_result.append(num*num)
    print('suarq_result is:',sum(square_result))  #since diffrent processes share diffrent memory space we cannot define this print statement below in driver code

def cube (arr):
    global cube_result
    for num in arr:
        time.sleep(0.2)
        print('cube:',num*num*num)
        cube_result.append(num*num*num)
    print('cube_result is:',sum(cube_result))

if __name__=='__main__':
    arr=[2,3,8,9]

    p1=multiprocessing.Process(target=square,args=(arr,))
    p2=multiprocessing.Process(target=cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    t=time.time()
    print('time taken:',t)
    

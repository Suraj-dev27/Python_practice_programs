import multiprocessing

# Sharing data between processes using  array and value

def square(arr,result,val):
    val.value = 5.67
    for idx, n in enumerate(arr):  #'idx' gives index and 'n' gives value
        result[idx]=n*n

if __name__=="__main__":
    arr=[2,3,5]
    result=multiprocessing.Array('i',3)  #here we are passing array of values
    val=multiprocessing.Value('d',0.0)  #here we are passing only single value

    p=multiprocessing.Process(target=square,args=(arr,result,val))
    p.start()
    p.join()
    
    print("square of shared array of values:",result[:])
    print("shared value is:",val.value)

#sharing data between processes using  queue

def square(munbers, q):
    for n in numbers:
        q.put(n*n)

if __name__=="__main__":
    numbers=[2,3,5]

    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=square,args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())

#using lock in multiprocessing
import time
def deposit(balance,lock):
    for i in range(100):   #this will add 100 rs 1 by 1 in balance
        time.sleep(0.01)
        lock.acquire()
        balance.value=balance.value+1
        lock.release()

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.aqcuire()
        balance.value=balance.value-1
        lock.release()

if __name__=='__main__':
    balance = multiprocessing.Value('i',200)
    lock=multiprocessing.Lock()
    d=multiprocessing.Process(target='deposit',args=(balance,lock))
    w=multiprocessing.Process(target='withdraw',args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
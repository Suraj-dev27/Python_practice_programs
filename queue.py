from collections import deque
'''class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)

pq=Queue()
pq.enqueue({'name':'suraj','id':10})
pq.enqueue({'name':'rohan','id':11})
pq.enqueue({'name':'shubham','id':16})
print(pq.buffer)
print(pq.size())
print(pq.is_empty())
print(pq.dequeue())'''

# exercise 1:
'''
Design a food ordering system where your python program,
Place Order: This will be placing an order and inserting that into a queue. This places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This will server the order. All you need to do is pop the order out of the queue and print it. This serves an order every 2 seconds. Also start this 1 second after place order is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,
orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order() is producing orders whereas server_order() is consuming the food orders. Use Queue class implemented in a video tutorial.
'''
import time
class Food_order:
    def __init__(self):
        self.buffer=deque()
        
    def place_order(self,val):
        for order in val:
            print("Placing order for:",order)
            self.buffer.appendleft(order)
            time.sleep(0.5)
        print(self.buffer)
        

    def recieve_order(self):
        

        time.sleep(1)
        while True:
            if len(self.buffer)==0:
                return("Queue is empty, no more orders")
            else:
                order= self.buffer.pop()
                print('Now serving:',order)
            time.sleep(2)


pq=Food_order()
pq.place_order(['pizza','samosa','pasta','biryani','burger'])
#pq.place_order('samosa')
#pq.place_order('pasta')
#pq.place_order('biryani')
#pq.place_order('burger')
#print(pq.buffer)
print(pq.recieve_order())


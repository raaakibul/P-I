# Data structure 
import queue

# numbers = [1,2,3,4,5,6,7,8]
# counter = 1

q = queue.Queue()
numbers = [10,20,30,40,50,60]
for number in numbers:
    q.put(number)
    # print(q.get())
print(q.get())
print(q.get())

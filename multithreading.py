import threading 

def hello_world():
    for x in range(50):
        print("Hello World")
    
def function():
    for x in range(100):
        print("One")
def function2():
    for x in range(100):
        print("Two")
    
t1 = threading.Thread(target=hello_world)
t1.start()
t1.join()
print("Another text")

t2 = threading.Thread(target=function)
t3 = threading.Thread(target=function2)

t2.start()
t3.start()
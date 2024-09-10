import threading 

def hello_world():
    print("Hello World")
    
t1 = threading.Thread(target=hello_world)
t1.start()

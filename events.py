import threading

event = threading.Event()

def myFunction():
    print("Waiting for event to trigger")
    event.wait()
    print("Performing action")
    
t1 = threading.Thread(target=myFunction)
t1.start()
    
x = input("Do you want to thrigger the event(y/n)?\n")
    
if x =='y':
    event.set()
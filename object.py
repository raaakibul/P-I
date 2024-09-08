class Person:
    def __init__(self,name, age, id):
        self.name = name
        self.age = age
        self.id = id
        
    def helloWorld(self):
        print("Hello World")
        
    def __del__(self):
        print("Object deleted")

x = Person("Mike", 22, 456)
print(x.name, x.age, x.id)
# print(x.age)

y = Person("Sarah", 21, 556)
print(y.name, y.age,y.id)


x.helloWorld()

del x
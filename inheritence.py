# inheritence 

class Person:
    
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        
    def __str__(self):
        return "Name: {},Age: {},Id: {}".format(self.name, self.age, self.id)
    
    def get_older(self,years):
        self.age += years

class Worker(Person):
    
    def __init__(self, name, age, id, salary):
        super(Worker, self).__init__(name, age, id)
        self.salary = salary       
    
    def __str__(self):
        text = super(Worker, self).__str__()
        text += ", Salary : {}".format(self.salary)
        return text
    
    def calc_yearly_salary(self, salary):
        return self.salary * 12
    
worker1 = Worker("Henry", 40, 145, 3000)
print(worker1)
print(worker1.calc_yearly_salary(1200)) 
    
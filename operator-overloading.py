# python allowed operator overloaded functions, c might be used i am not sure. 
# java doesn't allowed it

class Vector:
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return Vector(self.x + other.x, self.y+other.y)
    
    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)
    def __str__(self):
        return "x:{}, y:{}".format(self.x, self.y)
    
v1 = Vector(2,5)
v2 = Vector(6,3)
v3 = Vector(10,5)
v4 = Vector(6,4)

print(v1)
print(v2)

v_rsult = v1 + v2
print(v_rsult)

v_result2 = v1-v2
print(v_result2)

print(v3)
print(v4)

v_result3 = v3 + v4
v_result4 = v3-v4
print(v_result3)
print(v_result4)
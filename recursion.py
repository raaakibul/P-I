#non recursion way 
n = 7

fact = 1

while n>0:
    fact = fact * n
    n = n - 1
print(fact)

# recursion way

def factorial(x):
    if x <1:
        return 1
    else: 
        number = x * factorial(x-1)
        return number
result = factorial(8)
print(result)
def add (a, b):
    return a+b
def subtract (a, b):
    return abs(a-b)
def divide(a, b):
    if a < b: return int(b/a)
    if a > b: return int(a/b)
def multiply(a, b):
    return a*b
print("Arithmetics module is imported")

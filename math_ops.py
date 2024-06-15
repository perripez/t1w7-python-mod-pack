def add(*args):
    sum = 0
    for each in args:
        sum += each
    return sum

def subtract(*args):
    difference = 0
    for each in args:
        sum -= each
    return difference

def multiply(*args):
    multiply = 1
    for each in args:
        multiply *= each
    return multiply

def divide(a,b):
    if b == 0:
        return "Error! Diviaion by 0!"
    return a / b

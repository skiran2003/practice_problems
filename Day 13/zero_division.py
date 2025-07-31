def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide with zero"
    
print(divide(8,2))
print(divide(5,0))  # Zero Division Error
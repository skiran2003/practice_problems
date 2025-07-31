def division(a,b):
    try:
        a=int(a)
        b=int(b)
        try:
            print(a/b)      # Using try-except block within a try-except block
        except ZeroDivisionError:
            print("Cannot divide with Zero")
    except ValueError:
        print("Cannot convert to integer")

division(5,4)
division(8,0)
division('a',2)
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))
if n1>n2:
    if n2>n3:
        print(f'{n1} is the largest')
    elif n3>n1:
        print(f'{n3} is the largest')
elif n2>n3:
    print(f'{n2} is the largest')
else:
    print(f'{n3} is the largest')
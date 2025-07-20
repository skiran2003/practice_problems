def multiply(*num):
    p=1
    for i in num:
        p*=i
    return p
print(multiply(1,2,3,4,-2))
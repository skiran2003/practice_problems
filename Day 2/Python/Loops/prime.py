num=int(input("enter a number:"))
for i in range(2,num):
    for j in range(2,int(num**0.5)+1):
        if(i%j==0):
            if(i==j):
                continue
            break
    else:
        print(f'{i} is prime')
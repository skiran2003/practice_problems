def Solution(l,target):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==target:
                return [i,j]
l=[5,8,3,6,10]
target=8
res=Solution(l,target)
print(res)
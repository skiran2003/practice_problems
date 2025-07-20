# def left_rotation(l,k):
#     for i in range(k):
#         l.insert(0,l[-1])
#         l.pop()
#     return l
def right_rotation(l,k):
    for i in range(k):
        last=l.pop()
        l.insert(0,last)
    return l
l=[1,2,3,4]
k=2
# result1=left_rotation(l,k)
result2=right_rotation(l,k)
# print(result1)
print(result2)


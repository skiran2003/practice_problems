empty_list=[]
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
words=['a','b','hello']
mixed=[1,'abcd',{'key':'value'},(1,2,3),{1,2,3,4}]
# for i in mixed:
#     print(type(i))

for i in numbers:
    print(f"{i}\t {i:o}\t {i:X}\t {i:b}")
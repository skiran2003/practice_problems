# l1=[x**2 for x in range(1,11)]
# print(l1)
#############################################################
# With conditions

# evens=[x for x in range(1,11) if x%2==0]
# print(evens)
#############################################################
# Nested comprehension

matrix=[[i*j for j in range(3)] for i in range(3)]
print(matrix)
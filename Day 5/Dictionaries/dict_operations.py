# Creating a dictionary
d1={1:2,3:4} # Using {}
# d1={} Creates an empty dict
d2=dict(a=1,b=2) # Using dict() constructor

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# for x, obj in myfamily.items():
#     print(x)
    
#     for y in obj:
#         print(y + ':', obj[y])

x={1:2,3:4}
x.setdefault(4,7)
print(x)

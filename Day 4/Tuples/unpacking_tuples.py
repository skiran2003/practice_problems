def unpacking_tuples(t):
    for element in t:
        for i,j in (element.items() if isinstance(element,dict) else [element]):
           print(i)
           print(j)

t=([1,2],{'name':'Sai'})
# If print function is used it returns None because there is no return value in the function
unpacking_tuples(t) 

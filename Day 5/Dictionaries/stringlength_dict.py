def string_length(l):
    d={}
    for i in l:
        length=len(i)
        if length in d:
            d[length].append(i)
        else:
            d[length]=[i]
    return d

l=["hi", "hello", "sun", "day"]
print(string_length(l))
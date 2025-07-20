def count_occurences(l):
    d={}
    for i in l:
        c=l.count(i)
        d[i]=c
    return d
l=[1,2,3,1,2,1,4,4,5,2,3]
print(count_occurences(l))
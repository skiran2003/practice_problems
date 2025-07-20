l=[[1,2],[2,1],[3,4],[1,2]]
s1=set()
l2=[]
for i in l:
    s2=frozenset(i)
    if s2 not in s1:
        s1.add(s2)
        l2.append(i)
print(l2)
def remove_occurences(l,num):
    if num in l:
        c=l.count(num)
        if c>1:
            for i in range(c-1):
                l.remove(num)
        else:
            return "Only one occurence"
        return l
    else:
        return "Number not present in the list"

l=[1,4,4,4,5,3,8]
num=2
res=remove_occurences(l,num)
print(res)
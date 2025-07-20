def set_membership(s,i):
    if i in s:
        return True
    else:
        return False
    
s={1,6,8,2}
i=5
print(set_membership(s,i))
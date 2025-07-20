def check_key(d,k):
    if k in d:
        return True
    else:
        return False

d={'a':1,'b':2,'c':3}
k='c'
print(check_key(d,k))
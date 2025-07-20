def swap_items(d):
    d1={}
    for keys,values in d.items():
        d1.update({values:keys})
    return d1
d={'a':1,'b':2,'c':3}
print(swap_items(d))
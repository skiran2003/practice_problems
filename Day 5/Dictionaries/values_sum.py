def values_sum(d):
    sum=0
    for b in d.values():
        sum+=b
    return sum
d={'a':100,'b':200,'c':300}
print(values_sum(d))
# print(d.values())
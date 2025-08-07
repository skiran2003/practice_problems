from pattern import letters as lt
from pattern import numbers as num
from pattern import symbols as sym
from random import shuffle,choice

def letter(n):
    s1=''
    for i in range(n):
        s1+=choice(lt)
    return s1

def number(m):
    s2=''
    for i in range(m):
        s2+=choice(num)
    return s2

def symbol(n):
    s3=''
    for i in range(n):
        s3+=choice(sym)
    return s3

def password_generation(n,m,l):
    s=''
    s+=letter(n)+number(m)+symbol(l)
    s_list=list(s)
    shuffle(s_list)
    return ''.join(s_list)

pwd=password_generation(4,3,2)
print(pwd)
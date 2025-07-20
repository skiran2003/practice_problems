from collections import namedtuple

Books = namedtuple("Books",("Title Author Year"))
book = Books('1984','Orwell',1949)
b1=book._replace(Year=1952)
b=book._asdict()
print(b)
print(b1)
print(type(b1))
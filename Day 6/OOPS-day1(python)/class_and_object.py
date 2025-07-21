class Person:
    def __init__(person,name,age):
        person.name=name
        person.age=age
    def __str__(person):
        return f"Hello {person.name}! Welcome"

p=Person("Sai",22)
print(p)
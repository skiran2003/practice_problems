def person_info(**details):
    for keys,values in details.items():
        print(f'{keys}--->{values}')
        print(10*'*')
person_info(name='Kiran',age=22,department="CSE")
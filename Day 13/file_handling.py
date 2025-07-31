def read_file(file):
    try:
        f=open(file,'r')
        print(f.read())
    except FileNotFoundError:
        print("File not found")

read_file('sample.txt')
read_file('file1.json') # File not found error

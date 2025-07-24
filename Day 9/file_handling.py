def readfile(f):
    n=open(f,'r')
    print(n.read())

def writefile(f,text):
    n=open(f,'w')
    n.write(text)
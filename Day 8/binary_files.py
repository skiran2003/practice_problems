# Used for performing file handling operations on binary files, image files ... etc.
# Read mode
f=open(r"C:\Users\pc\Downloads\laptop.jpg",'rb') # 'rb' means read binary mode
print(f.read()) # prints the byte code of the image file

# Writing from one binary file to other binary file
f1=open("C:/Users/pc/Downloads/laptop.jpg",'rb')
f2=open("C:/Users/pc/Downloads/laptop_1.jpg",'wb')
for i in f1:
    f2.write(i) # Copy the image to new file

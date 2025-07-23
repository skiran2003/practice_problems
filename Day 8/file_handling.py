#Creating a file
f=open("Sample.txt",'x') # 'x' defines that the file is in create mode

# {Raises an error if the file already exists}
f.write("File created Successfully ! ")
f.close() # An open file must be closed to avoid resourse leaks

# Reading the file
o=open("Sample.txt",'r') # 'r' defines that the file is in read mode # Cursor points at the beginning of the file
print(o.read())
print(o.read(2)) # read specified number of characters
print(o.readline()) # reads each single line in the file
print(o.readlines()) # returns each line as a list element
o.close()

# Writing into a file
a=open('Sample.txt','w') #'w' defines that the file is in write mode
a.write("The file content is rewritten") # Erases the existing content and the writes the given content into the file

# # Writes the list of lines as each single line in the file
a.writelines(['This is an example of write operation\n','The writelines() method writes the given lines into the file'])
a.close()

# Appending into a file
a=open('Sample.txt','a') # 'a' defines that the file is in append mode # Cursor points at the end of the file
a.write("Now the file is in append mode") # Does not erase the existing content and starts adding contents from where the cursor is placed
# writelines() method also can be used to append content into a file
a.close()

# Using with statement
with open('Sample.txt','r') as a:  # The with statement closes the file automatically, So no need to close() the file
    print(a.read())

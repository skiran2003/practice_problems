# Read and Write mode

f=open("new.doc",'r+')
print(f.read()) # Reads the contents of the file
print(f.tell()) # Tells about the position of the cursor
f.write("\nWe are performing read + write operations in file handling")

# Write and Read mode

f=open("new_1.doc",'w+') # Creates a new file if file does not exist
f.write("We created a new file Successfully...!")
print(f.read()) # Prints nothing because the cursor goes to end of the file after writing
f.seek(2) # Moves the cursor to the specified position
print(f.tell())
print(f.read())

# Append and Read mode

f=open('new_1.doc','a+') # Creates a new file if file does not exist
# f.write("We are using append and read mode:")
print(f.tell())
f.seek(0) # Moves the cursor to the beginning of the file
print(f.read())
import os

# os module should be imported to remove files
os.remove("Sample.txt") # Deletes the file(If file does not exist raises an error)

if os.path.exists("Sample.txt"): # Checks if the file exists in the path or not before deleting
    os.remove("Sample.txt")

if os.path.isfile("Sample.txt"): # Checks if it is a file or not
    os.remove("Sample.txt")

os.rmdir("Sample folder") # Removes a folder (Only if it is empty)

if os.path.isdir("New directory"): # Checks if the folder is directory or not
    os.rmdir("New directory")

# Renaming files
os.rename('sample.doc','new.doc') # renames a file

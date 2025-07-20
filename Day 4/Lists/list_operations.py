# List Operations
#############################################################################################################
# ADDING ITEMS
list_1=[1,2,3]
list_1.append({1:25}) # Adds at the end #[1,2,3,{1:25}] --> adds the item as it is
list_1.insert(2,{4:5})
list_1.extend([4,5]) # Items are added as individual elements #cannot add dictionary to the list, Only key will be added
print(list_1)

l1=[1,2,3]
d1={4:5}
l1.extend(d1)
print(l1)

################################################################################################################
# DELETING ITEMS
l1=[4,5,6,7]
l1.pop(2) #removes items at the given index(if index not specified deletes from end)
l1.remove(7) # Removes the specified item from the list
del l1[2] # Deletes at the specified index
del l1  # Deletes the entire list
l1.clear() # Deletes all the elements from the list and leaves empty list
print(l1)

################################################################################################################
# COUNT, SORTING AND REVERSING
l1=[1,2,2,2,5,4,3,3,7,9,6,6,6,6,6]
print(l1.count(6)) # counts the number of occurences of an element in the list
l1.sort() # Sorts the list in ascending order
l1.reverse() # Reverse the list elements
print(l1)
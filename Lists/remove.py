# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)



# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)


# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
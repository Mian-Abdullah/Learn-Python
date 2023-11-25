""" In Python, we can enter multiple value in a single Variable using List.
We can create a list by using [] to make a list
The benefit of the list is that we can store the large amount of data as the name of a student or subjects of class. It
is not necessary that we have to enter the data of the same type we enter a different type of data. In this way, the
list is different from Arrays. In Array, we have to enter the same type of data. However, in a list we can enter the
data of different types, and also Array is non-primitive or user define data type like function, but the list is
primitive or build in data type"""

l1 = [3, 5, 234, 234, "Abdullah"]
# When we check the type of List, we came to know that it is a Class 'list' a build in data type in python
print(type(l1))
print(l1)

'''One property of string is that string is immutable that means string once made cannot be changed but if you'll say 
we did slicing of string. We made string -->> name = "abdullah". Once I made name = "abdullah" either we can change the 
name once again but we cannot change the string if we write print this, print(name[0:3]), so new string will be created 
in python that mean python has to create a new string and inside it there are 0 to 3 characters. So by doing "name[0:3]"
new string is created but this is no need to create a new list in list, you can modify that list. That mean we can 
add or remove anything from the above list using a method called l1.remove() mean list name.remove()'''

l1.remove("Abdullah")
print(l1)
'''So this won't return a new list, it will remove from the above list. So I don't need to print this because I'm simply
giving a command. We need to understand the difference that in the string slicing have printed everything because new 
string is forming everytime it slice a string but here when we are running command l1.remove() it mean remove from the 
l1 so this means modify l1 directly'''
print(l1.count(234))  # Remember here it is not returning a list, it is returning a number to I have to use print.
'''A method that modify the list like if Iuse sort. So I'll only l1.sort() and this will sort the whole list... 
existing list because list is mutable. 
Remember that list is mutable will strings are not.'''
l1.sort()  # Sort mean arranging from ascending to descending
print(l1)
# There are alot of method to modify like
l1.pop()  # If we remove the last element from the list
print(l1)
l1.append(99)  # It will add 999 in the list
print(l1)
l1.clear()  # It will empty and clear the complete list
print(l1)
l1.copy()  # It will make a copy of the list
print(l1)
l1.extend([211, 67, 28, "Ali"])  # It will extend or expand the list. It is very helpful when we want to add an element
# of 1 list into list 2
print(l1)
print(l1.index(67))  # It will tell the index of an element
print(l1[0:2])  # List Slicing
l1[0] = "Python"  # It will assign Python value to 0th index value of a list
print(l1)

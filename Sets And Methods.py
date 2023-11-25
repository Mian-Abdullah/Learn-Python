a1 = {3, 5, 23, 5, 5, 5, "Abdullah"}  # This is a Set in Python
# In set, it will consider one element only One time, if we repeat it will consider it only the first time it is used
print(a1)
# You can see we get {3, 23, 5, Abdullah} in print because 5 was already present in the set it wasn't counted again
# If you don't know, What is Set? -->> There is a concept of set in Mathematical Theory -->> Set is a collection of
# well-defined objects --- If you want to know more about a set, you can check it on Google by searching sets in math
# and sets in python
a2 = {3, 5, 23, "Abdullah"}
# Both a1 and a2 are same and equal in a set.
# If I write "a1." I will get a list of method in sets suggested by pycharm
a1.clear()  # It will empty the set.
print(a1)
print(a2)
print(a2.pop())  # It will give me a random element from the set -->> This time it popped 3 from the set might be next
# it will popp any other element from the set
print(a2)  # Now I would not get 3 in the set because it is popped
a1.add(2)  # It will add an element in the a1 set
print(a1)
print(a1.union(a2))  # Give me the union(all elements) of a1 and a2
print(a1.intersection(a2))  # Give the Intersection(Common elements) of a1 and a2
# If you want to understand all the methods that you have to study the set theory to understand it more efficiently.
# The one thing you have to always check in set and other data types is that which method is retuning a new set or data
# type and which is updating the existing sat and data type.

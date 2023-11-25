dict1 = {}
b = {}
print(dict1, type(dict1))
print(b, type(b))
# Both dict1 and b are a Dictionary not an empty set it looks like an empty set, but actually it is not an empty set;
# then the question is how we can create an empty set, We can create an empty set by writing "c = set()"
c = set()  # It is an empty set in python; it is how an empty set look like in python. {} is used to indicate dictionary
print(c, type(c))

# A Dictionary is a key value pair -->> Just like our Oxford Dictionary
dict2 = {"Good": "Something Pleasant", "Fetch": "To Bring", "1": "The Number 1"}
print(dict2["Good"])
# Suppose we want to store the marks of students
marks = {"Faizan": 99.9, "Abdullah": 99, "Asad": 89, "Bilal": 92, "Muzamil": 40, "Sahal": 45, "Moozam": 70,
         "Murtaza": 50}
print(marks["Abdullah"])
print(marks["Moozam"])
# In the above, every name is a key when I call any name it will fetch the value corresponding to that key
# Dictionary is mutable, why? -->> because we can change it
marks["Hafiz Umer"] = 65  # Add it in the mark dictionary
print(marks)
# We can also check the method by writing "marks." and pycharm will show me all the methods of dictionary
print(marks.get("Faizan Freed"))  # It will return empty dictionary because Faizan Freed don't exist in the dictionary
# It shows output None which mean the value corresponding to Faizan Freed in None
print(marks.get("Faizan"))  # It will show the value corresponding to Faizan, which is 99.9
# Why do we need get method I can simply write print(marks["Faizan"]) it get the same answer with the get method -->>
# You are right, but if you write a word that did not exist in dictionary like I write Faizan Freed  in simple print,
# I will get error, but if I use get method it will output None telling that there in no value corresponding to Faizan
# Freed The .get method save me from error
print(marks.keys())  # Show us all the keys of the Dictionary
print(marks.values())  # It gives us the values of the Dictionary
print(marks.items())  # Give us the tuples of key value pairs

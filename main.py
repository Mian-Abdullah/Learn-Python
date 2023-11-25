# 1.First Python Program
print("Hello World!")
print('Hello Abdullah')  # Hey AJ

# 2. Short Keys in PyCharm
# Ctrl + D are used to duplicate lines in PyCharm. I can also get multiple cursors using Alt.
# Just press Alt on keyboard and click on places where you need multiple cursors
# To move lines up and down we can use Alt + Shift + Up/Down key

# 3.Comments
# Comments: This a comments in Python (code in comments doesn't execute by compiler will ignore that code) and
# also its short key is Ctrl + /
# Multi Line Comments we use
'''
Hi
Every
one 
this 
is 
Abdullah
'''

# 4.Variable in Python --> In python we use variable to store Data
# Integer or int Data Type
a = 3
print(a)
b = 55
print(b)
# Float Data Type
a = 6.2
print(a)
# Boolean Variable or Data Type
# or False
c = True
print(c)
# String Data Type
d = "Harry"
print(d)
# None Data Type
e = None
print(e)
# Other Data Types are bytes, set, lists, dictionary, tuples and complex, etc.


# 5.Typecasting --> converting things from one datatype to another
f = "9"
print(f)
g = 9
print(g)
'''Now let's discuss does both of these are same than the answer is yes or no ---> Yes because both have the 9 ---> 
No because if we observe deeply f is string and g is an integer type variable like if i try to print print(f +1) 
----> Here i will get error because i cannot add 1 in a string to resolve this we can convert f into an integer like 
this print(int(f) + 1) print(g + 1) ----> Here it didn't get any error because it is alright to add 1 in an integer 
similarly and vise versa'''

# 6.Concatenation --> It is the concept of obtaining a new string by joining two different strings that both are
# original strings.
String1 = "My name is"
String2 = "Abdullah"
print(String1 + " " + String2)

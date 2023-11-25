# 7.Operators in Python
"""
Rules to write operator in Python
we cannot give space between the name of Operators like num 1
the name of operators cannot start with a number like 2num
the name of operator can start from the _ like _num.
We cannot start the name of operator from the special character
"""
num1 = 10
num2 = 3
# Arithmetic Operators
print("num1 + num2 is ", num1 + num2)
print("num1 * num2 is ", num1 * num2)
print("num1 - num2 is ", num1 - num2)
print("num1 / num2 is ", num1 / num2)
print("num1 // num2 is ", num1 // num2)  # Convert float number into int
print("num1 ** num2 is ", num1 ** num2)  # It takes power it mean give answer of 10 ki power 3 ka
print("num1 % num2 is ", num1 % num2)  # Give the reminder after the division

# Assignment Operator
a = 4
# a += 2
# print(a)
# a -= 2
# print(a)
# a /= 2
# print(a)
a *= 2
print(a)

# Comparison Operators
x = 8
y = 3
z = 8
print(x > y)
print(x < y)
print(x != y)
print(x == z)

# Logical Operators
print(x == z and x < y)  # Both conditions should be fulfilled than answer will be true otherwise false
print(x == z or x < y)  # One condition should be fulfilled than answer will be true otherwise false
print(not False)  # The Inverse the condition means change True into False and False into True
print(not True)

# 9. User Input Method
name = input("Enter your Name ")  # Passing any message is not necessary I can simply use input function for user input
print(type(name))  # Tell the data type of function or variable
# Input Function always populates our variable as a string either user enters a number that viable data type will
# remain the string
print(name)
# Now when you run name it allow me to enter my name, and when I write my name and press Enters, it will print it


# Write a python program to take a number from user as an input and add "6" into it
num = input("Enter a Number ")
print(num)
print(type(num))
# The answer we get is that num is a string so, now if we want to add "6" to it, we have to do TypeCasting
# If we don't do TypeCasting we got error that we cannot add 6 in the num because num is a string and 6 is integer
# TypeCasting change the Datatype of a Variable to the desired data type
print(int(num) + 6)


Abdullah = 1
abdullah = 2
# In Python, the Variable name a Case Sensitive like above both Abdullah and abdullah are two different variables.


a = 'Abdullah1'
b = "Abdullah2"
c = '''Abdullah 
is a good boy'''
d = 'Abdullah'\
    'in Lahore'  # Using "\" we can also create a multi-line string
# In Python, we can create string using single citation, double citation or either using triple citation all are
# correct methods. The triple citation is mostly used to make multi-line strings
print(Abdullah, abdullah, a, b, c, d)  # In print statement, we can print mutltiple things using coma(,).

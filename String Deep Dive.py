# 8. String and String Methods
name = 'abdullah'
number = "7"
# I can create a string by both either using single '' or ""
print(name)
# String Slicing
print(name[0:3])  # It means start from zero and goes all the way till to 2 (3-1)
print(name[1:4])  # It means start from one and goes all the way till to 3 (4-1)
# print(name[a:l])# It mean starts from a and goes all the way till to l-1


# String Methods
print(name.upper())  # It will Uppercase the complete String
print(name.capitalize())  # If the String-first letter is small, it will capitalize it
print(name.count("l"))  # It is used to know how many times a word is used in a string
print(name.isalnum())  # It checks that is the string is makeup of alphabet and numerical characters
print(number.isalpha())  # Its check is string have any alphabet or not


'''One property of string is that string is immutable that means string once made cannot be changed but if you'll say 
we did slicing of string. We made string -->> name = "abdullah". Once I made name = "abdullah" either we can change the 
name once again but we cannot change the string if we write print this, print(name[0:3]), so new string will be cerated 
in python that mean python has to create a new string and inside it there are 0 to 3 characters. So by doing "name[0:3]"
new string is cerated but this is no need to create a new list in list, you can modify that list'''
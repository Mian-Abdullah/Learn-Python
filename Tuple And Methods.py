t = (3, 5, 23, 23, 5, 'Abdullah')  # This is a Tuple, like string is immutable, tuple is immutable too
print(t)
# So, the main point of tuple is that we cannot change the tuple. Like if I write t. In pycharm so i can't any suggested
# method which can change the tuple
print(t.count(5))  # Used check how much time a number is used
print(t.index(23))  # Used to check the index of a value in a tuple
# The difference between Tuple and List is that we cannot change the tuple anyway
# Like if I try to do "t[0] = 89" which mean give value 89 to the value of 0 Index of tuple then we will get an error
# -->> "Tuple object does not support item assignment", I will get the same error if I try to do this to the string but
# if I do this with List, it will happen because list is mutable while string and tuple are immutable

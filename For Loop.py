"""The For Loop is very simple use to repeat somthing, again and again like I have to write, "I love Python" 3 time
it is very simple I will use print function 3 times and print it, but what about when I have to write like 300 or
3000 times. I know it sounds crazy but just for the sake of example, if I have to type it 300 or 3000 times I cannot
use print function or if you use copy and paste method firstly it takes a lot of time also might be I forget counting
and print less or more time for the solution of this we have loops"""
for i in range(10):  # Range function starts from 0
    print(i + 1)
# If you +1 with "i" then it will print from 1 to 10, and if I simply use "i" it will print from 0 to 9
# We can also use For Loop with List
a = [1, 34, 456, 34, 234]
for item in a:
    print(item)  # It will print all the item of list one by one
# What does For Loop do -->> in any list or any iterator value it print one by one, It can be tuple It can be keys of
# Dictionary It can a set it's not compulsory it should be a list It works for my other iterables means
# which can be iterated whose values can be enumerated one by one
s = {265, 000, 456, "Abdullah"}
print("Printing Set...")
for item in s:
    print(item)  # The values of the set don't come in order keep this in mind

# In this way we can print any message in python as much time I need
for _ in range(500):
    print("I love Python")

# Break in the For Loop
for i in range(3):
    if(i == 3):
        break
    print(i+1)
# Now what will happen when "i" value will become 3 it will exit the loop
# Continues in the For Loop
for i in range(5):
    if(i == 3):
        continue # It will say that go for the new value of the "i"
    print(i+1)
# Continue, on the other Hand, says that run for the next loop value stopping here, For example, what will be the "i"
# next value, first value is 0 next will be 1 after that 2 then 3 and 4 it will go from 0 to 4 when we write rang 5.
# In this case, "i" value will be 0 at first and 1 will get printed when I will be 1, 2 will be printed when "i" will
# be 2, 3 will be printed when "i" will be 3, 4 will not get printed because we said to continue when "i" value will
# be 3 which mean's don't execute down below and run it for 4 value after this it will run for "i" value 4 and 5 will
# be printed

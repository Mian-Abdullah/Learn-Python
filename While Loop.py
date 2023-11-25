# While Loop is very similar to For Loop,
# What While Loop does is suppose I created a variable "i = 0"  Now suppose I say while(i<10) the print "i" and then
# make "i+ =1", so what will happen is first of all, this condition will get checked whether i<10 if it is true then it
# will go inside the loop and then print the "i" and then "i" will be updated, "i +=1" is the updating statement, The
# upgrading continue until the condition of 10 will be statisfied or true
i = 0
while (i < 10):
    print(i)
    i += 1
print("Program has be finished executed...")
# It will also work like this
i = 0
while i < 10:
    print(i)
    i += 1
print("Program has be finished executed...")

# Infinite While Loop -->> The While Loop that will never end
# while True:  # We can also write it -->> while(True):
#     print("While Loop is not Finishing")
# Sometimes there is a point of running an infinite while loop

while (True):
    num = int(input("Enter a number: "))
    print(num)
    if (num == 0):
        break  # It will exit the loop -->> In other words, it means to break this loop and get out -->> there are
        # only 2 conditions one is "continue", and the other is "break" -->>
        # We can also use break with For Loop if we want to
print("Program has finished executing...")
# Now if I enter any number, it will take it. However, as soon as I enter 0 here it will print me "Program has finished
# executing..."; Now this was an infinite loop, but here I created a way to break it, so sometimes this loop is also
# beneficial for as in some ways


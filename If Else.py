age = int(input("Enter your Age: "))  # It is a shortcut method to convert string input into int
# Condition 1
if (age >= 18):  # We can also write like "if age>=18:"
    # Here if I write 18, I will get output "No, You can go Home" because in age > 18 mean age = 18 is false. If I want
    # to change and want that when I enter 18, it will show me output "Yes, You can Drive" than with age I will use
    # age >= 18
    print("Yes, You can Drive")
# Condition 2
elif (age == 1):  # elif mean elseif in python -->> also write it "elif ==1:"
    print("You are a Kid")
# Condition 3
elif (age == 10):  # Write this like "elif age == 10:"
    print("You are a Decade Kid")
# Condition 4
else:
    print("No, You can go Home")
# End of Program
print("Program Ended")
# Now the Running structure of the Program is that First user have to enter age than program check condition 1 if
# satisfied print its message than at last it will print Program Ended otherwise check condition 2 and 3 which one
# satisfied it will show it message than at last it will print Program Ended

# If I write something different like Abdullah or Abdullah1 in age that I will get error that these are not integer.
# One more important thing is that we can also only use If without ele it will also work fine. But we cannot start
# with elif with if it is an error and the last this if and elif will also work fine it is not necessary we have to
# end program on else we can also end it on elif if we want to so, else statement is not necessary, but it is good
# practice

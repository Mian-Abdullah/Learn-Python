# Match Case is a new statement is a new addition in Python 3.10 onwards
a = int(input("Enter a Number: "))
# In the match case statement we match the variable with the case then print the message which is written in the case
# like in the above variable if user enters 1 It will match with case 1, and user will see the message "Case is 1"
# So what Match Case do? -->> It does that according to a variable's value, It will run the code snippets
match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 3:
        print("Case is 3")
    case 22:
        print("Case is 22")
    case _:  # It will show a default statement when no case matched it I don't add this default then if no case will
        # match user would not see any message
        print("No Match found")

# Can we do this with If / Else? -->> We can, but somewhere this thing will become convenient and fast.
# Quiz: Write a python program to print the table of number which lies between 1 and 10
b = int(input("Enter your Number between 1 to 10 to see the table: "))
match b:
    case 1:
        print(
            "Here is your Table of 1\n"
            "1 x 1 = 1\n" 
            "1 x 2 = 2\n"
            "1 x 3 = 3\n"
            "1 x 4 = 4\n"
            "1 x 5 = 5\n"
            "1 x 6 = 6\n"
            "1 x 7 = 7\n"
            "1 x 8 = 8\n"
            "1 x 9 = 9\n"
            "1 x 10 = 10"
        )
    case 2:
        print(
            "Here is your Table of 2\n"
            "2 x 1 = 2\n"
            "2 x 2 = 4\n"
            "2 x 3 = 6\n"
            "2 x 4 = 8\n"
            "2 x 5 = 10\n"
            "2 x 6 = 12\n"
            "2 x 7 = 14\n"
            "2 x 8 = 16\n"
            "2 x 9 = 18\n"
            "2 x 10 = 20"
        )
    case 3:
        print(
            "Here is your Table of 3\n"
            "3 x 1 = 3\n"
            "3 x 2 = 6\n"
            "3 x 3 = 9\n"
            "3 x 4 = 12\n"
            "3 x 5 = 15\n"
            "3 x 6 = 18\n"
            "3 x 7 = 21\n"
            "3 x 8 = 24\n"
            "3 x 9 = 27\n"
            "3 x 10 = 30"
        )
    case 4:
        print(
            "Here is your Table of 4\n"
            "4 x 1 = 4\n"
            "4 x 2 = 8\n"
            "4 x 3 = 12\n"
            "4 x 4 = 16\n"
            "4 x 5 = 20\n"
            "4 x 6 = 24\n"
            "4 x 7 = 28\n"
            "4 x 8 = 32\n"
            "4 x 9 = 36\n"
            "4 x 10 = 40"
        )
    case 5:
        print(
            "Here is your Table of 5\n"
            "5 x 1 = 5\n"
            "5 x 2 = 10\n"
            "5 x 3 = 15\n"
            "5 x 4 = 20\n"
            "5 x 5 = 25\n"
            "5 x 6 = 30\n"
            "5 x 7 = 35\n"
            "5 x 8 = 40\n"
            "5 x 9 = 45\n"
            "5 x 10 = 50"
        )
    case 6:
        print(
            "Here is your Table of 6\n"
            "6 x 1 = 6\n"
            "6 x 2 = 12\n"
            "6 x 3 = 18\n"
            "6 x 4 = 24\n"
            "6 x 5 = 30\n"
            "6 x 6 = 36\n"
            "6 x 7 = 42\n"
            "6 x 8 = 48\n"
            "6 x 9 = 54\n"
            "6 x 10 = 60"
        )
    case 7:
        print(
            "Here is your Table of 7\n"
            "7 x 1 = 7\n"
            "7 x 2 = 14\n"
            "7 x 3 = 21\n"
            "7 x 4 = 28\n"
            "7 x 5 = 35\n"
            "7 x 6 = 42\n"
            "7 x 7 = 49\n"
            "7 x 8 = 56\n"
            "7 x 9 = 63\n"
            "7 x 10 = 70"
        )
    case 8:
        print(
            "Here is your Table of 8\n"
            "8 x 1 = 8\n"
            "8 x 2 = 16\n"
            "8 x 3 = 24\n"
            "8 x 4 = 32\n"
            "8 x 5 = 40\n"
            "8 x 6 = 48\n"
            "8 x 7 = 56\n"
            "8 x 8 = 64\n"
            "8 x 9 = 72\n"
            "8 x 10 = 80"
        )
    case 9:
        print(
            "Here is your Table of 9\n"
            "9 x 1 = 9\n"
            "9 x 2 = 18\n"
            "9 x 3 = 27\n"
            "9 x 4 = 36\n"
            "9 x 5 = 45\n"
            "9 x 6 = 54\n"
            "9 x 7 = 63\n"
            "9 x 8 = 72\n"
            "9 x 9 = 81\n"
            "9 x 10 = 90"
        )
    case 10:
        print(
            "Here is your Table of 10\n"
            "10 x 1 = 10\n"
            "10 x 2 = 20\n"
            "10 x 3 = 30\n"
            "10 x 4 = 40\n"
            "10 x 5 = 50\n"
            "10 x 6 = 60\n"
            "10 x 7 = 70\n"
            "10 x 8 = 80\n"
            "10 x 9 = 90\n"
            "10 x 10 = 100"
        )
    case _:
        print("You enter number other that 1 to 10")
# Try Except Exception Handling
"""I have created a program in which whatever number the user enters will have '+ 3' added to it. The program works
fine as long as the user enters a number. However, what happens if a user enters a string instead of a number? If you 
ask why a user might do this, the simple answer is that they are the user; they can do it intentionally, or it might
be a mistake. But when a user enters a string instead of a number, an error occurs. The program cannot prevent the 
user from doing this. For example, 'Mark Zuckerberg' created 'Facebook.' If we comment wrong, he won't come and say 
'do not do this' or 'if I try to drag a profile photo,' he will not say 'do not do this' because we haven't added 
that function. It's not the programmer's responsibility to handle the errors. However, I created the program, 
so it is my duty to handle its errors too. I am the programmer and I have to handle the errors because user will come in
bulk if your app is public, so they will do as they wish, It is not in my control what they will do, it's their wish,
their internet, their home, their computer, everything is theirs they can do anything they want. If it affects your
server then it's your responsibility, so you have to do error handling, you can blame user for any error, In mobile you
use application as I want it's not like you would be given instruction don't tap here I don't add here function or
listener, it is not possible"""
try:
    a = int(input("Enter your number "))
    print(a + 3)
# except:
except Exception as e:
    # some this we also want to show what error is concurring than we use "e" and then we can print "e" with the error
    # message, or I can send this error to my server log for help or details, simple except will also work fine
    print("Some error occurred", e)  # This "e" is printing the error
# Now if a user enters any string instead of number then, it will show it the except message
# Try Except mean to try this if this does not happen then run the except part now program will not crash
# A programmer always want to make its application alive when any error comes the application become dead to save this
# programmer use try except to show error message

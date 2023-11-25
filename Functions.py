# Function is a very strong part of any programing language -->> Function means you can separate the logic from a
# program, The function will run only when I call that function
def greetHello():  # Here I have created a Function of name "greetHello" with the help of "def" keyword
    # It is a good practice to have the function name in lower case
    # "def" is a reserved keyword in the python after which we give a space then we write a function name as we wish in
    # this case I have written "greetHello", I can name anything, Below I can write print as many time as I need, I can
    # also use loop in it if you want to
    print("Hello")
    print("Hi")
    print("Hey")
    # The above function is printing "Hello", now if I want to run this function, then I just have to type "greatHello"


print("Executing Function...")  # This will run before running the function
greetHello()
print("Execution Done")  # This will run after function


# I can also pass arguments in the function
def sayHello(name, ending):
    print("Hey there " + name)  # This is a string concatenation
    print(ending)
    # String concatenation refers to the process of combining two or more strings into a single string. In most
    # programming languages, concatenation is done using an operator (often the + symbol) or a specific
    # method/function that joins strings together end-to-end.


# From def to ending is a registered function so the code it will not run until I call it, the execution will start
# from the print below

# Now in the function I have to pass two things, one is name and the other is ending
print("Execution Started")
sayHello("Abdullah", "Thank You")
# The great thing about this function is that I can reuse it with other argument like below
sayHello("Asad", "Done Boss")
print("Execution Done")


# The name and ending are the arguments of the function that we have to pass while executing the function, and we can
# use them in the function


# We can write a function which can generate a letter on the basis of template
def letterGenerator(name, date):
    st = f"Hi Sir!\nThis is {name}. I cannot come to University on {date}."
    # \t (ued for double space), \n is a simple character but written in two characters and used to start the next
    # message from new line
    print(st)
    # This is an "fString" -->> When ever I make fString this is called fString when you put "f" before the string
    # With the help of fString we can use variable in the string like I use name in the string


letterGenerator("Abdullah", "November 24,2023")
letterGenerator("Asad", "November 30,2023")

print("Letter Generated")

# We can also create a new function that will find the average of two numbers, and it will return something; you have
# seen all the function I have written above they are not returning something they are just printing, if they didn't
# print anything, then we will never know that the function is running
def average(a, b):
    return (a+b)/2

print(average(2, 6))
# Now what will happen is that the function take the value of a and b the add them and at last divide it by 2and
# return and print us the answer
# It is not nesseasary we build a function, we also have some build in function in the python like print function
# some time we can use function using the modules. We get the function as the part of package that we install from pip


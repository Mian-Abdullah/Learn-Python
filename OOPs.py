# Here classes, methods, function, objects we discuss these Why do we use Class? -->> Class is like a template which
# is used to make object, just like we go to the railway station reservation to book your ticket on the railway
# counter, you go and say give me the form he will give you a black form, suppose another person Asad go for
# reservation he will give him the same form to be filled out for reservation, same goes on the third person Bilal
# and so on, The form will be the same that will be given to the every person want to reserve the seat but the form
# will become different from each other when the passengers fill their details in it. I have my on form, Asad has its
# own form, Bilal has own and so on
# So class is a template form that you can make objects -->> The class will be a blank reservation form and the object
# will be the filled railway reservation form

# Class and their Methods
class Employee:
    salary = 89
    name = "Abdullah"
    def getSalary(self):
       return self.Salary()

Abdullah = Employee
print(Abdullah.salary)
print(Abdullah.name)
# The above things are ok. However, I want to make separate Employees here comes the concept of Constructors -->>
# Constructor is a function that automatically runs when an object is created like if you write any function inside
# class then first argument self is automatically passed -->> Self is the reference of that object for which this
# method is being called

class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary


Asad = Employees("Asad", 2000)  # Changed "2000" to 2000 (integer)
print(Asad.name)
print(Asad.salary)

Bilal = Employees("Bilal", 1111)
print(Bilal.name)
print(Bilal.salary)

# Is this type of programing is necessary, the answer is no when can do the same work using functions but we use it
# to deal with and create real world entities -->> Like I am creating a game like  GTA 5 for this I can create a
# class name "pedestrian" which have method like "pedestrian.walk", .fight, .run etc., so OOPs makes things easy to
# understand -->> It is difficult to learn OOPs and Modelling to make classes is kind of difficult but using them
# easy that we will feel great. You might hate OOPs, but here is an important thing that OOPs is not used as much in
# Python -->> that a big statement but let me tell you it is not used that much If you are doing Machine Learning or
# Data Science you will use a lot of classes but not write a lot of classes a lot of mean not you will never write a
# class, If you ask can I say this about C++, I cannot because we create a lot of classes in C++,I am not saying don't
# learn it, learning will never hurt

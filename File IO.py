# In Projects alot of time we want that we can store data or read write that from file for this we use file I/O
# In File I/O we have three modes 1. Read -->> read files 2. Write -->> write in the file 3. Append -->> Appends a file
# What is Appending -->> so when ever we write a file it will empty the file that mean deletes all the existing content
# of that file add the content we want to add, but sometimes we don't want to delete the existing content and just want
# to increment the content here we use Append
s = "Abdullah is a Good Boy"
# Suppose I have create a string `s = "Abdullah is a Good Boy"` and Now I want to write it in a file then I will use one
# of the following methods


# Writing a file Using Context Manager -->> "with" keyword is the context manager it will automatically close file
# with open("test.txt", "w") as f:
#     f.write(s)

# Writing a file Without context manager -->> Long Method
fp = open("text.txt", "w")  # "w" represent the mode
fp.write(s)
fp.close()
# I can also use "f" instead of "fp" it is a variable name


# Reading a file using context manager
with open("Read.txt", "r") as f:
    r = f.read()
    print(r)

# Reading a file without context manager
f = open("Read.txt", "r")
r = f.read()
print(r)
# It is not necessary to write this, but it is a good practice it will close that file and save us from errors
f.close()


# Appending a file using context manager
with open("Appends.txt", "a") as f:
    f.write("Hey Abdullah")
# Appending a file without context manager
f = open("Appends.txt", "a")
f.write("AJ Group")
f.close()
# There is a safe delete option in the Pycharm -->> Which mean if I am trying to delete a file which have a using in my
# project file, then pycharm will ask me is it safe to delete this file it will also show me where that file is using
# after if I want to delete that file, I can

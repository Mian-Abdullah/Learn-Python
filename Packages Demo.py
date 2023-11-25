""" Modules and Pip -->> Python have the Pip with the help of which we can download Modules --> Module mean code written by
other person --> Like there is Python library on Google name Pandas --> To download any package we use command "pip
install package name" --> in macOS we also have to write python version with pip --> To download pandas we open our
terminal in PyCharm and write "pip install pandas" and it will be downloaded and to import we use keyword import and
then package name """

import pandas as pd

# As with package name we can create short name for big name
df = pd.read_excel("file.xlsx")
# To use pandas, we also have to download the openpyxl by command "pip install openpyxl"
print(df)


# Other packages used in python are "scikit-learn" for machine learning
# pdfreader to read pdf file --> PYPDF2 to merge to pdfs


# Indentation
def func1():
    # This is a function and it the method to create function in python
    print(3)  # The space before print tell it is inside the function and the space is called indentation

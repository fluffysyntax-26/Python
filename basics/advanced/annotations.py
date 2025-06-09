# demonstrates annotation (type declaration in python)
import typing # import the typing module to annotate sequence data types

name: str = "Deepak"
age: int = 19
height: float = 163.67

print(name, age, height)

# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]

# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)

# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}

# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}

'''
Type annotation allows you to clearly communicate the argument types and return type of functions in your code. 
It’s like giving yourself and other developers hints about what kind of data the variable is supposed to hold.
This has several benefits: It reduces the chance of common mistakes, helps in documenting your code for others to reuse, 
and allows integrated development software (IDEs) and other tools to give you better feedback.
'''
# help('keywords')

"""
Python is case-sensitive
Indentation is important
Semi-colons are not required
variables can't be keywords
Title case for classes (class PersonName)
lowercase for variables and functions
uppercase= constant (by convention)
no need to declare data types exclusively
"""

name= 'Ram'
print(type(name))

age= 23

#Input
word = input('Enter any word: ')
print(word)

#Output
print("My name is", name, " and age is", age, ".")
print("My name is {} and age is {}.".format(name, age))
print(f"My name is {name} and age is {age}.")

#Type casting: implicit and explicit
print(int('5')+2)
print(float(5))
print("It is day " + str(4))

print(type(age))
print(type(str(age)))
print(type(float(age)))


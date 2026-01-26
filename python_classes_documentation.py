# Python OOP

# What is OOP?
'''
OOP stands for Object-Oriented Programming.

Python is an object-oriented language, allowing you to structure
your code using classes and objects for better organization and
reusablitiy.
'''

# Advantages of OOP
'''
* Provide a clear structure to programs
* Makes code easier to maintain, reuse, and debug
* Helps keep your code DRY (Don't Repeat Yourself)
* Allows you to build reusable applications with less code

Tip : The DRY principle means you should avoid writing the same
code more than once.
Move repeated code into functions or classes and reuse it.
'''

# What are Classes and Objects?
'''
Classes and objects are the two core concepts in object-oriented
programming.

A class defines what an object should look like, and an object is
created based on that class. For example:

Class -> Objects
---------------------------------------------
Fruit -> Apple, Banana, Mango
Car -> Toyota, IKCO, Volvo, Audi

When you create an object from a class, it inherits all the
variables and functions defined inside that class.
'''

# 1- Python Classes and Objects
# Python Classes/Objects
'''
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties
and methods.
A Class is like an object constructor, or a 'bluprint' for 
creating objects.
'''

# Create a Class

class MyClass:
    x = 5

# Create Object

p1 = MyClass()
print(p1.x)
print("-------------------")

# Delete Objects
del p1

# Multiple Objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)
print("-------------------")

'''
Note: Eech object is independent and has its own copy of the class
properties.
'''

# The pass Statement
'''
class definitions cannot be empty, but if you for some reason have
a class definition with no content, put it the pass statement to
avoid getting an error.
'''

class Person:
    pass

# 2- Python __init__() Method

'''
All classes have a built-in method called __init__(), which is
always executed when the class is being initiated.

The __init__() method is used to assign values to object 
properties, or to perform operations that are necessary when
the object is being created.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Hamed', 30)
print(p1.name)
print(p1.age)
print("-------------------")

'''
Note: The __init__() method is called automatically every time
the class is being used to create a new object.
'''

# Why Use __init__() ?
'''
Without the __init__() method, you would need to set properties
manually for each object:
'''
class Person:
    pass

p1 = Person()
p1.name = 'Hamed'
p2.age = 30

print(p1.name)
print(p2.age)
print("-------------------")

class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Hamed', 30)

print(p1.name)
print(p1.age)
print("-------------------")

# Default Values in __init__()
class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

p1 = Person('Hamed')
p2 = Person('Ali', 26)

print(p1.name, p1.age)
print(p2.name, p2.age)
print("-------------------")

# Multiple Parameters
'''
The __init__() method can have as many parameters as you need:
'''

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person('Hamed', 30, 'Tehran', 'Iran')
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
print("-------------------")

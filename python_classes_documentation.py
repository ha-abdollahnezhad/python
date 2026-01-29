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

# 3- Python self Parameter
'''
The self parameter is a reference to the current instance of the
class.
It is used to access properties and methods that belong to the class.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello, my name is : ' + self.name)
p1 = Person('Hamed', 18)
p1.greet()
print("-------------------")

'''
Note: The self parameter must be the first parameter of any
method in the class

Why Use self?
Without self, Python would not know which object's properties you
want to access:
'''
class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

p1 = Person('Hamed')
p2 = Person('Ali')

p1.print_name()
p2.print_name()
print("-------------------")


'''
self Does Not Have to Be Named "self"
It does not have to be named self, you can call it whatever you
like, but it has to be the first parameter of any method in the
class:
'''
class Person:
    def __init__(myObject, name, age):
        myObject.name = name
        myObject.age = age

    def greet(abc):
        print('Hello, my name is '+ abc.name)
    
p1 = Person('Hamed', 20)
p1.greet()
print("-------------------")

'''
Note: While you can use a different name, it is strongly
recommended to use self as it is the convention in Python and 
makes your code more readable to others.
'''

# Accessing Properties with self
# You can access any property of the class using self:

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f'{self.year} {self.brand} {self.model}')
car1 = Car('Toyota', 'Landcruser', 2026)
car1.display_info()
print("-------------------")

# Calling Methods with self
# You can also call other methods within the class using self:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return 'Hello, ' + self.name
    def welcome(self):
        message = self.greet()
        print(message + '! Welcome to our website.')

p1 = Person('Hamed')
p1.welcome()
print("-------------------")

# 4- Class Properties
'''
Properties are variables that belong to a class. They store data
for each object created from the class.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Hamed', 18)
print(p1.name)
print(p1.age)
print("-------------------")

# Access Properties
# You can access object properties using dot notation:

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car('Toyota', 'Landcruser')
print(car1.brand)
print(car1.model)
print("-------------------")

# Modify Properties
# You can modify the value of properties on objects:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Ali", 5)
print(p1.age, p1.name)

p1.age = 3
print(p1.age, p1.name)
print("-------------------")

# Delete Properties
# You can delete properties from objects using del keyword:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Hamed', 30)
del p1.age
print(p1.name)
# print(p1.age) # This would cause an error
print("-------------------")

# Class Properties vs Object Properties
'''
Properties defined inside __init__() belong to each 
object (instance properties).
Properties defined outside method belong to the class 
itself (class properties) and are shared all objects:
'''

class Person:
    species = 'Human'
    def __init__(self, name):
        self.name = name

p1 = Person('Hamed')
p2 = Person('Ali')

print(p1.name, p1.species)
print(p2.name, p2.species)
print("-------------------")

# Modifying Class Properties
# When you modify a class property, it affects all objects:

class Person:
    lastname = ''

    def __init__(self, name):
        self.name = name
p1 = Person('Ali')
p2 = Person('Hamed')

Person.lastname = 'Alavi'

print(p1.name, p1.lastname)
print(p2.name, p2.lastname)
print("-------------------")

# Add New Properties
# You can add new properties to existing objects:

class Person:
    def __init__(self, name):
        self.name = name
p1 = Person('Ali')
p1.age = 4
p1.city = 'Najaf'

print(p1.name, p1.age, p1.city)
print("-------------------")

'''
Note: Adding properties this way only adds them to that specific
object, not to all objects of the class.
'''

# 5- Python Class Methods
# Class Methods

'''
Methods are functions that belong to a class. They define the
behavior of objects created from the class.
'''
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, my name is ' + self.name)

p1 = Person('Ali')
p1.greet()
print("-------------------")

'''
Note: All methods must have self as the first parameter.
'''
# Methods with Parameters
# Methods can accept parameters just like regular functions:

class Calculator:
    def add(self, a, b):
        return a+b
    def multiply(self, a, b):
        return a*b
    
calc = Calculator()
print(calc.add(10, 30))
print(calc.multiply(10, 30))
print("-------------------")


# Methods Accessing Properties
# Methods can access and modify object properties using self:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f'{self.name} is {self.age} years old'
    
p1 = Person('Hamed', 20)
print(p1.get_info())
print("-------------------")

# Methods Modifying Properties
# Methods can modify the properties of an object:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def celebrate_birthday(self):
        self.age += 1
        print(f'Happy birthday! You are now {self.age}')

p1 = Person('Hamed', 18)
p1.celebrate_birthday()
p1.celebrate_birthday()
print("-------------------")

# The __str__() Method
'''
The __str__() method is a special method that controls what is 
returned when the object is printed:
'''

# Without the __str__() method:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Hamed', 30)
print(p1)
print("-------------------")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} ({self.age})'
    
p1 = Person('Ali', 20)
print(p1)
print("-------------------")

# Multiple Methods
# A class can have multiple methods that work together:

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f'Added: {song}')
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f'Removed: {song}')
    def show_songs(self):
        print(f'Playlist \'{self.name}\':')
        for song in self.songs:
            print(f'- {song}')

my_playlist = Playlist('Favorites')
my_playlist.add_song('karevan')
my_playlist.add_song('shohada')
my_playlist.show_songs()
print("-------------------")

# Delete Methods
# You can delete methods from a class using del keyword:

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print('Hello!')
p1 = Person('Hamed')

del Person.greet
# p1.greet() This will cause an error
print("-------------------")

# 6- Python Inheritance
'''
Inheritance allows us to define a class that inherits all the 
methods and properties from another class.

Parent class is the class being inherited from, also called
base class.

Child class is the class that inherits from another class, also
called derived class.
'''

# Create a Parent Class
'''
Any class can be a parent class, so the syntax is the same as
creating any other class:
Create a class named Person, with firstname and lastname 
properties, and a printname method:
'''

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def print_name(self):
        print(self.firstName, self.lastName)

x = Person('Ali', 'Mohammadi')
x.print_name()
print("-------------------")

# Create a Child Class
'''
To create a class that inherits the functionality from another
class, send the parent class as a parameter when creating the 
child class:

Create a class named Student, which will inherit the properties
and methods from the Person class:
'''

class Student(Person):
    pass

'''
Note: Use the pass keyword when you do not want to add any other
properties or methods to the class.
'''

x = Student('Hamed', 'Alavi')
x.print_name()
print("-------------------")

# Add the __init__() Function
'''
So far have create a child class that inherites the properties
and methods from its parent.
We want to add the __init__() function to the child class
(instead of the pass keyword).

Note: The __init__() function is called automatically every time
the class is being used to create a new object.
'''

class Student(Person):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_student_name(self):
        print('Student : ',self.fname, self.lname)

x = Student('Hamed', 'Alavi')
x.print_student_name()
print("-------------------")

'''
When you add the __init__() function, the child class will no
longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance
of the parent's __init__() function.

To Keep the inheritance of the parent's __init__() function, add
a call to the parent's __init__() function:
'''
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init(self, fname, lname)

'''
Now we have successfully added the __init__() function,
and kept the inheritance of the parent class, and we are ready
to add functionality in the __init__() function.
'''

# Use the super() Function
'''
Python also has a super() function that will make the child class
inherit all the methods and properties from its parent:
'''

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

'''
By using the super() function, you do not have to use the name
of the parent element,
it will automatically inherit the methods and properties from 
its parent.
Add a property called graduationYear to the Student class:
'''

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationYear = 2020

'''
In the example below, the year 2020 should be a variable, and
passed into the Student class when creating student objects. To
do so, add another parameter in the __init__() function:
'''

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year
x = Student('Hamed', 'Alavi', 2020)

# Add Methods

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year

    def welcome(self):
        print('Welcome', self.firstName, self.lastName, 'to the class of', self.graduationYear)

x = Student('Hamed', 'Abdollah', 2020)
x.welcome()
print("-------------------")

'''
If you add a method in the child class with the same name as a
function in the parent class, the inheritance of the parent
method will be overridden.
'''

# 6- Python Polymorphism
'''
The word 'polymorphism' means 'many forms', and in programming
it refers to methods/functions/operators with the same name that can be
executed on many objects or classes.
'''
# Class Polymorphism
'''
Polymorphism is often used in Class methods, where we can have multiple
classes with the same method name.

for example, say we have three classes: Car, Boat, and Plane, and they
all have a method called move():
'''

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print('Fly!')

car1 = Car('Toyota', 'Landcruser')
boat1 = Boat('Ibiza', 'Touring 20')
plane1 = Plane('Boeing', '747')

for x in (car1, boat1, plane1):
    x.move()
print("-------------------")

'''
Look at the for loop at the end. Because of polymorphism we can execute
the same method for all three classes.
'''

# Inheritance Class Polymorphism
'''
What about classes with child classes with the same name? Can we use
polymorphism there?

Yes. if we use the example above and make a parent class called Vehicle,
and make Car, Boat, Plane child classes of Vehicle, the child classes
inherits the Veicle methods, but can override them:
'''

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print('Move!')
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print('Sail!')

class Plane(Vehicle):
    def move(self):
        print('Fly!')

car1 = Car('Toyota', 'Landcruser')
boat1 = Boat('Ibiz', 'Touring 20')
plane1 = Plane('Boeing', '747')

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
print("-------------------")

'''
Child classes inherits the properties and methods from the parent class.
In the example above you can see that the Car class is empty, but it
inherits brand, model, and move() from Vehicle.

The Boat and Plane classes also inherit brand, model, and move() from
Vehicle, but they both override the move() method.
Because of polymorphism we can execute the same method for all classes.
'''

# 7- Python Encapsulation
'''
Encapsulation is about protecting data inside a class.
It means keeping data(properties) and methods to gether in a class,
while controlling how the data can be accessed from outside the class.
This prevents accidental changes to your data and hides the internal
details of how your class works.
'''

# Private Properties
'''
In Python, you make properties private by using a double underscore
__ prefix:
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private property

p1 = Person('Hamed', 12)
print(p1.name)
# print(p1.__age) # This will cause an error
print("-------------------")

'''
Note: Private properties cannot be accessed directly from outside
the class.
'''

# Get Private Property Value
'''To Access a private property, you can create a getter method:'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
p1 = Person('Ali', 62)
print(p1.get_age())
print("-------------------")

# Set Private Property Value
'''To modify a private property, you can create a setter method.
The setter method can also validate the value before setting it:'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('age must be positive number')
p1 = Person('Ali', 62)
print(p1.name, p1.get_age())

p1.set_age(-6)
print(p1.name, p1.get_age())

# Why Use Encapsulation?
'''
Encapsulation provides several benefits:
* Data Protection: Prevents accidental modification of data.
* Validation: You can validate data before setting it.
* Flexibility: Internal implementation can change without affecting 
externa code.
* Control: You have full control over how data is accessed and modified.
'''

class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print('Grade must be between 0 and 100')
    def get_grade(self):
        return self.__grade

    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"
        
student = Student('Hamed')
student.set_grade(100)
print(student.name, student.get_grade(), student.get_status())
print("-------------------")

# Protected Properties
'''Python also has a convention for protected properties using a
single underscor _ prefix:'''

class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary # Protected property

p1 = Person('Ali', 999999999999999999999999999)
print(p1.name)
print(p1._salary)
print("-------------------")

'''
Note: A single underscore _ is just a convention. It tells other
programmers that the property is intended for internal use, but
Python doesn't enforce this restriction.
'''

# Private Methods
'''
You can also make methods private using the double underscore prefix:
'''

class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True
    
    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print('Invalid number')
calc  = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # this would cause an error
print("-------------------")

'''
Note: Just like private properties with double underscores, private
methods cannot be called directly from outside the class.
The __validate method can only be used by other methods inside the class.
'''

# Name Mangling
'''
Name mangling is how Python implements private properties and methods.
When you use double underscore __ , Python automatically renames it 
internally by adding _ClassName in fornt.
For example, __age becomes _Person__age.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
p1 = Person('Ali', 63)
# this is how Python mangles the name:
print(p1._Person__age) # Not recommended!
print("-------------------")

'''
Note: While you can access private properties using the mangled name,
it's not recommended. It defeats the purpose of encapsulation.
'''

# 8- Python Inner Classes
'''
An inner class is a class defined inside another class. The inner class
access the properties and methods of the outer class.

Inner classes are useful for grouping classes that are only used in one
place, making your code more organized.
'''

class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print('This is the inner class')

outer = Outer()
print(outer.name)
print(outer.Inner().name)
print("-------------------")

# Accessing Inner Class from the Outside
'''
To access the inner class, create an object of the outer class, and then
create an object of the inner class:
'''

class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"
        def display(self):
            print(f'Hello from {self.name}')

outer = Outer()
inner = outer.Inner()
inner.display()
print("-------------------")

# Accessing Outer Class from Inner Class
'''
Inner classes in Python do not automatically have access to the outer
class instance.
If you want the inner class to access the outer class, you need to pass
the outer class instance as a parameter:
'''
class Outer:
    def __init__(self):
        self.name = 'Outer'

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print(f'Outer class name: {self.outer.name}')

outer = Outer()
inner = outer.Inner(outer)
inner.display()
print("-------------------")

# Practical Example
'''
Inner classes are useful for creating helper classes that are only
used within the context of the outer class:
'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine():
        def __init__(self):
            self.status = 'Off'

        def start(self):
            self.status = 'Running'
            print('Engine started')
        def stop(self):
            self.status = 'Off'
            print('Engine stopped')
    def drive(self):
        if self.engine.status == 'Running':
            print(f'Driving the {self.brand} {self.model}')
        else:
            print('Start the engine first')

car = Car('Toyota', 'Landcruser')
car.drive()
car.engine.start()
car.drive()
print("-------------------")

# Multiple Inner Classes
'''A Class can have multiple inner classes:'''
class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print('Processing data...')

    class RAM:
        def store(self):
            print('Storing data...')
computer = Computer()
computer.cpu.process()
computer.ram.store()
print("-------------------")

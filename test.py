# 1- first app
print("hellow every one")

# 2- python version
import sys
print(sys.version)

# 3- python indentation
if False:
    print("this will work when condition result is true")
else:
    print("this will work when condition result is false")


# 4- python comments
# # -> use for line comment
# """ -> use for multi line comment

# 5- python statements
print("hello i'm hamed.")
"""
if we want write several statements in a single line should use semeicolon (;)
next statement will print content in new line
"""
print("hello ");print("i'm ");print("hamed.")

# 6- print without a new line

print("hello every body", end=" ")
print("i'm learning python.")

# 7- python variables
x = 14
y = "x is : "
print(y,x)
print(type(x))
x = 'sally'
print(y,x)
print(type(x))

X=14 # variable names are case-sensitive
print("x ==> ",x,type(x), "X ==> ", X,type(X))
    # casting
a = str(5)
b = int(5)
c = float(5)

print(a, " ", b, " ", c)

# 8- variable names
"""
legal variable names
    myvar, my_var, _my_var, myVar, MYVAR, myVar2

illegal variable names
    2myvar, my-var, my var

multi words variable namesd
    camel case => myVariableName = "hamed"
    pascal case => MyVariableName = "hamed"
    snake case => my_variable_name = "hamed"

"""

# 9- assign values
x, y, z = "red", "green", "blue"
print(x)
print(y)
print(z)

x = y = z = "pink"
print(x, " ",y," ",z)

    # Unpack a collection
cars = ['tiba', 'pars', 'quick', 'soren', 'dena']

a, b, c, d, e = cars
print(a," ",b," ",c," ",d," ",e)

# 10- global variable
x = 'awesome'
def myFunction():
    global x
    x='fantastic'
    print(x)
myFunction()
print(x)

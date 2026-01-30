# 1- Python File Open
'''
File handling is an important part of any web application.
Python has several function for creating, reading, updating, and
deleting files.
'''
# File Handling
'''
The key function for working with files in Python is the open() funciton.
The open() function takes two parameters: filename, and mode.
There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file
does not exist.
"a" - Append - Opens a file for appending, creates the file if it does
not exist.
"w" - Write - Opens a file for writing, creates the file if it does not
exist.
"x" - Create - Creates the specified file, returns an error if the file
exists.

In addition you can specify if the file should be handled as binary or 
text mode

"t" - Text - Default value. Text mode.
"b" - Binary - Binary mode (e.g. images)
'''

# Syntax
# To open a file for reading it is enough to specify the name of the file

f = open('demofile.txt', 'w')
f.write('This is new content for test\n')
# The code above is the same as :
f = open('demofile.txt', 'rt')
'''
Because "r" for read, and "t" for text are the default values,
you do not need to specify them.
Note: Make sure the file exists, or else you will get an error.
'''

# Open a File on the Server
# Assume we have the following file, located in the same folder as Python:
# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method
# for reading the content of the file:

f = open('demofile.txt')
print(f.read())
print("-------------------")

# If the file is located in a different location, you will have to 
# specify the file path, like this:

f = open("C:\\Users\haabd\python\demofile.txt")
print(f.read())
print("-------------------")

# Using the with statement
# You can also use the with statement when opening a file:

with open('demofile.txt') as f:
    print(f.read())
print("-------------------")
# Then you do not have to worry about closing your files, the with statement
# takes care of that.

# Close Files
'''
It is a good practice to always close the file when you are done with it.

If you are not using the with statement, you must write a close statement
in order to close the file:
'''
f = open('demofile.txt')
print(f.readline())
f.close()
print("-------------------")

'''
Note: You should always close your files. In some cases, due to buffering,
changes made to a file may not show until you close the file.
'''

# Read Only Parts of the File
'''
By default the read() method returns the whole text. but you can also
specify how many characters you want to return:
'''
with open('demofile.txt') as f:
    print(f.read(5))
print("-------------------")

# Read Lines
'''
You can return one line by using the readline() method:
'''

with open('demofile.txt') as f:
    print(f.readline())
print("-------------------")

# By calling readline() two times, you can read the two first lines:

with open('demofile.txt') as f:
    print(f.readline())
    print(f.readline())
print("-------------------")

# By looping through the lines of the file, you can read the whole file,
# line by line:

with open('demofile.txt') as f:
    for x in f:
        print(x)
print("-------------------")

# 2- Python File Write
'''
To write to an existing file, you must add a parameter to the open()
function:
"a" - Append - Will append to the end of the file
"w" - Write - Will overwrite any existing content 
'''
with open('demofile.txt', 'a') as f:
    f.write('\nNow the file has more content!')

# open and read the file after the appending:
with open('demofile.txt') as f:
    print(f.read())
print("-------------------")

# Overwrite Existing Content
'''
To overwrite the existing content to the file,
use the w parameter
'''
with open('demofile.txt', 'w') as f:
    f.write('Woops! I have deleted the content!')
# Open and read the file after the owerwriting:
with open('demofile.txt') as f:
    print(f.read())
print("-------------------")

'''
Note: the "w" method will overwrite the entier file.
'''

# Create a New File
'''
To create a new file in Python, use the open() method, with one of the
following parameters:
"x" - Create - will create a file, returns an error if the file exists
"a" - Append - will create a file if the specified file does not exists
"w" - Write - will create a file if the specified file does not exists
'''
# f = open('myfile.txt', 'x')
f = open('myfile.txt', 'w')
f.write('This is new text file...!')
print("-------------------")

'''
Note: If the file already exist, an error will be raised.
'''

# 3- Python Delete file
'''
To delete a file, you must import the OS module, and run its os.remove()
function:
'''

import os
# os.remove('demofile.txt')

# Check if File exist:
'''
To avoid getting an error, you might want to check if the file exist
before you try to delete it:
'''

import os
if os.path.exists('demofile.txt'):
    os.remove("demofile.txt")
    print("demofile.txt deleted successfully")
else:
    print('The file does not exist')
print("-------------------")

# Delete Folder
'''
To delete an entire folder, use the os.rmdir() method:
'''

import os
os.mkdir('myfolder')
print('Folder myfolder created successfully')
if os.path.exists('myfolder'):
    os.rmdir('myfolder')
    print('Folder myfolder deleted successfully')
else:
    print('Folder myfolder does not exist')
print("-------------------")

'''
Note: You can only remove empty folders.
'''
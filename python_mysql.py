import mysql.connector

# Create Connection

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "Ha@5040258194",
    port = 3306
)

print(mydb)
'''Now you can start querying the database using SQL statements.'''

# Creating a Database
'''
To create a database in MySQL, use the "CREATE DATABASE" statement:
'''

myCursor = mydb.cursor()
# myCursor.execute("CREATE DATABASE pyTestDB") # it would be executed at first time that you want create database.

# Check if Database Exists
'''
You can check if a database exist by listing all databases in your system
by using the "SHOW DATABASES" statement:
'''

myCursor.execute("SHOW DATABASES")

for x in myCursor:
    print(x)

'''Or you can try to access the database when making the connection:'''

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ha@5040258194',
    port = 3306,
    database = 'pyTestDB'
)

'''If the database does not exist, you will get an error.'''
import mysql.connector

# Create Connection

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "Ha@5040258194",
    port = 3306
)

print(mydb)
print("--------------------")

def check_database_exists(dbName):
    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES LIKE %s", (dbName,))
    result = cursor.fetchone()
    #cursor.close()
    #mydb.close()
    return result is not None


def check_table_exists(tbName):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "Ha@5040258194",
    port = 3306,
    database = 'pytestdb'
    )
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES LIKE %s", (tbName,))
    result = cursor.fetchone()
    #cursor.close()
    #mydb.close()
    return result is not None

'''Now you can start querying the database using SQL statements.'''

# 1- Creating a Database
'''
To create a database in MySQL, use the "CREATE DATABASE" statement:
'''
myCursor = mydb.cursor()
# myCursor.execute("CREATE DATABASE pyTestDB")


# Check if Database Exists
'''
You can check if a database exist by listing all databases in your system
by using the "SHOW DATABASES" statement:
'''
db_exists = check_database_exists('pytestdb')
if not db_exists :
    myCursor.execute("CREATE DATABASE pyTestDB")

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

# 2- Python MySQL Create Table
# Creating a Table
'''
To create a table in mysql, use the "CREATE TABLE" statement.
Make sure you define the name of the database when you create
the connection.
'''
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ha@5040258194',
    port = 3306,
    database = 'pyTestDB'
)
myCursor = mydb.cursor()
# myCursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# Check if Table Exists
'''
You can check if a table exist by listing all tables in your database
with the "SHOW TABLES" statement:
'''
myCursor.execute('SHOW TABLES')
for x in myCursor:
    print(x)
print("--------------------")

tb_exist = check_table_exists('customers')
if not tb_exist :
    myCursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

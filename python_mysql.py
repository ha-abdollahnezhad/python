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
print("--------------------")

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

myCursor.execute('DROP TABLE customers')
tb_exist = check_table_exists('customers')
if not tb_exist :
    myCursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), address VARCHAR(255))')


# Primary Key
'''
When creating a table, you should also create a column with a uniqe key
for each record.
This can be done by defining a PRIMARY KEY.
We use the statement 'INT AUTO_INCREMENT PRIMARY KEY' which will insert
a uiqe number for each record. Starting at 1, and increased by one for
each record.
'''

# myCursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), address VARCHAR(255))')

'''
If the table already exist, use the ALTER TABLE keyword:
'''

# myCursor.execute('ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')

# 3- Python MySQL Insert Into Table
# Insert Into Table
'''
To fill a table in MySQL, use the "INSERT INTO" statement.
'''

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Ali", "Najaf")
myCursor.execute(sql, val)

mydb.commit()
print(myCursor.rowcount, "record inserted.")
print("--------------------")

'''
Important!: Notice the statement: mydb.commit(). It is required to make
the changes, otherwise no changes are made to the table.
'''

# Insert Multiple Rows
'''
To insert multiple rows into a table, use the executemany() method.
The second parameter of the executemany() method is a list of tuples,
containing the data you want to insert:
'''

sql = 'INSERT INTO customers (name, address) VALUES(%s, %s)'
val = [
    ('Hamed', 'Tehran'),
    ('Hasan','Ardebil'),
    ('Mohammad', 'Esfahan'),
    ('Mahdi', 'Tabriz'),
    ('Hossein', 'Khorasan Razavi'),
    ('Abolfazl', 'Qom'),
    ('Amir Ali', 'Zanjan'),
    ('Sadegh', 'Rasht'),
    ('Vahid', 'Oruomie')
]
myCursor.executemany(sql, val)
mydb.commit()
print(myCursor.rowcount, 'Record Was Inserted.')
print("--------------------")

# Get Inserted ID
'''
You can get the id of the row you just inserted by asking the cursor
object.

Note: If you insert more than one row, the id of the last inserted row
is returned.
'''

sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
val = ('Mahdi', 'Qom')
myCursor.execute(sql, val)
mydb.commit()
print(myCursor.rowcount, 'record inserted, ID is :', myCursor.lastrowid)
print("--------------------")

# 4- Python MySQL Select From
# Select From a Table

'''
To select from a table in MySQL, use the 'SELECT' statement:
'''

myCursor.execute('SELECT * FROM customers')
result = myCursor.fetchall()
for x in result:
    print(x)
print("--------------------")

'''
Note: We use the fetchall() method, which fetches all rows from the last
executed statement.
'''

# Selecting Columns
'''
To select only some of the columns in a table, use the 'SELECT' statement
followed by the column name(s):
'''
myCursor.execute('SELECT name, address FROM customers')
result = myCursor.fetchall()
for x in result:
    print(x)
print("--------------------")

# Using the fetchone() Method
'''
If you are only interested in one row, you can use the fetchone() method.
The fetchone() method will return the first row of the result:
'''

myCursor.execute('SELECT * FROM customers')
result = myCursor.fetchone()
print(result)
print("--------------------")

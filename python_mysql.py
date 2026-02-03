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
cursor = mydb.cursor(buffered=True)
# cursor.execute("CREATE DATABASE pyTestDB")


# Check if Database Exists
'''
You can check if a database exist by listing all databases in your system
by using the "SHOW DATABASES" statement:
'''
db_exists = check_database_exists('pytestdb')
if not db_exists :
    cursor.execute("CREATE DATABASE pyTestDB")

cursor.execute("SHOW DATABASES")

for x in cursor:
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
cursor = mydb.cursor(buffered=True)
# cursor.execute("CREATE TABLE customers (name VARCHAR(50), city VARCHAR(50))")


# Check if Table Exists
'''
You can check if a table exist by listing all tables in your database
with the "SHOW TABLES" statement:
'''
cursor.execute('SHOW TABLES')
for x in cursor:
    print(x)
print("--------------------")

cursor.execute('DROP TABLE customers')
tb_exist = check_table_exists('customers')
if not tb_exist :
    cursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), city VARCHAR(255))')


# Primary Key
'''
When creating a table, you should also create a column with a uniqe key
for each record.
This can be done by defining a PRIMARY KEY.
We use the statement 'INT AUTO_INCREMENT PRIMARY KEY' which will insert
a uiqe number for each record. Starting at 1, and increased by one for
each record.
'''

# cursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), city VARCHAR(255))')

'''
If the table already exist, use the ALTER TABLE keyword:
'''

# cursor.execute('ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')

# 3- Python MySQL Insert Into Table
# Insert Into Table
'''
To fill a table in MySQL, use the "INSERT INTO" statement.
'''

sql = "INSERT INTO customers (name, city) VALUES (%s, %s)"
val = ("Ali", "Najaf")
cursor.execute(sql, val)

mydb.commit()
print(cursor.rowcount, "record inserted.")
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

sql = 'INSERT INTO customers (name, city) VALUES(%s, %s)'
val = [
    ('Hamed', 'Tehran'),
    ('Hasan','Ardebil'),
    ('Mohammad', 'Esfahan'),
    ('Mahdi', 'Tabriz'),
    ('Hossein', 'Khorasan Razavi'),
    ('Abolfazl', 'Qom'),
    ('Amir Ali', 'Zanjan'),
    ('Sadegh', 'Rasht'),
    ('Vahid', 'Oruomie'),
    ('Majid', 'Tehran'),
    ('Hadi', 'Najaf'),
    ('Reza', 'Karbala'),
    ('Javad', 'Tehran')
    ]
cursor.executemany(sql, val)
mydb.commit()
print(cursor.rowcount, 'Record Was Inserted.')
print("--------------------")

# Get Inserted ID
'''
You can get the id of the row you just inserted by asking the cursor
object.

Note: If you insert more than one row, the id of the last inserted row
is returned.
'''

sql = 'INSERT INTO customers (name, city) VALUES (%s, %s)'
val = ('Mahdi', 'Qom')
cursor.execute(sql, val)
mydb.commit()
print(cursor.rowcount, 'record inserted, ID is :', cursor.lastrowid)
print("--------------------")

# 4- Python MySQL Select From
# Select From a Table

'''
To select from a table in MySQL, use the 'SELECT' statement:
'''

cursor.execute('SELECT * FROM customers')
result = cursor.fetchall()
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
cursor.execute('SELECT name, city FROM customers')
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")

# Using the fetchone() Method
'''
If you are only interested in one row, you can use the fetchone() method.
The fetchone() method will return the first row of the result:
'''

cursor.execute('SELECT * FROM customers')
result = cursor.fetchone()
print(result)
print("--------------------")

# 5- Python MySQL Where
# Select With a Filter

'''
When selecting records from a table, you can filter the selection
by using the 'WHERE' statement:
'''

sql = "SELECT * FROM customers WHERE city = 'Qom'"
cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")

# Wildcard Characters
'''
You can also select the records that start, includes, or ends with
a given letter or phrase.
Use the % to represent wildcard characters:
Select records where the city contains the word 'om'
'''

sql = 'SELECT * FROM customers WHERE city LIKE "%om%"'
cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")

# Prevent SQL Injection
'''
When query values are provided by the user, you should escape the
values.
This is to prevent SQL injections, which is a common web hacking
technique to destroy or misuse your database.
The mysql.connector module has method to escape query values:
Escape query values by using the placeholder %s method:
'''
sql = 'SELECT * FROM customers WHERE city = %s'
val = ('Tehran',)
cursor.execute(sql, val)
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")

# 6- Python MySQL Order By
# Sort the Result

'''
Use the ORDER BY statement to sort the result in ascending or
descending order.
The ORDER BY keyword sorts the result ascending by default. To
sort the result in descending order, use the DESC keyword.
'''

sql = 'SELECT * FROM customers ORDER BY name'
cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")

# ORDER BY DESC
'''Use the DESC keyword to sort the result in a descending order'''
sql = "SELECT * FROM customers ORDER BY name DESC"
cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")


# 7- Python MySQL Delete From By
# Delete Record
'''
You can delete records from an existing table by using the "DELETE FROM"
statement:
'''

sql = 'DELETE FROM customers  WHERE name = "Hamed"'
cursor.execute(sql)
mydb.commit()
print(cursor.rowcount, 'record(s) deleted')
print("--------------------")

'''
Important!: Notice the statement: mydb.commit(). It is required to
make the changes, otherwise no changes are made to the table.

Notice the WHERE clause in the DELETE syntax: The WHERE clause
specifies which record(s) that should be deleted, If you omit the
WHERE clause, all records will be deleted!
'''

# Prevent SQL Injection
'''
It is considered a good practice to escape the values of any
query, also in delete statements.
This is to prevent SQL injections, which is a common web hacking
technique to destroy or misuse database.
The mysql.connector module uses the placeholder %s to escape values
in the delete statement:
'''

sql = 'DELETE FROM customers WHERE city = %s'
val = ('Esfahan',)

cursor.execute(sql, val)
mydb.commit()
print(cursor.rowcount, 'record(s) deleted')
print("--------------------")


# Python MySQL Drop Table
# Delete a Table
'''
You can delete an existing table by using the "DROP TABLE" statement:
'''
tb_exist = check_table_exists('users')
if not tb_exist :
    cursor.execute('CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), password VARCHAR(50), email VARCHAR(255))')

sql = 'DROP TABLE users'
cursor.execute(sql)

# Drop Only if Exist
'''
If the table you want to delete is already deleted, or for any 
other reason does not exist, you can use the IF EXISTS keyword 
to avoid getting an error.
'''
sql = 'DROP TABLE IF EXISTS users'
cursor.execute(sql)

# 8- Python MySQL Update Table
# Update Table

'''You can update existing records in a table by using the
"UPDATE" statement:'''

sql = "UPDATE customers SET city = 'Kordestan' WHERE id = 14"
cursor.execute(sql)
mydb.commit()
print(cursor.rowcount, 'record(s) affected')
print("--------------------")

'''
Important!: Notice the statement: mydb.commit(). It is required
to make the changes,
otherwise no changes are made to the table.

Notice the WHERE clause in the UPDATE syntax: The WHERE clause
specifies which record or records that should be updated. If
you omit the WHERE clause, all records will be updated!
'''

# Prevent SQL Injection
'''
It is considered a good practice to escape the values of any query,
also in update statements.
This is to prevent SQL injections, which is a common web hacking
technique to destroy or misuse your database.
The mysql.connector module uses the placeholder %s to escape values
in the update statement:
'''
sql = 'UPDATE customers SET city = %s WHERE id = %s'
val = ('Tehran', 8)
cursor.execute(sql, val)
mydb.commit()
print(cursor.rowcount, 'record(s) affected')
print("--------------------")

# Python MySQL Limit
# Limit the Result
'''
You can limit the number of records returned from the query, by 
using the 'LIMIT' statement:
Select the 5 first records in the 'customers' table:
'''

cursor.execute('SELECT * FROM customers LIMIT 5')
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")

# Start From Another Position
'''
If you want to return five records, string from the third record,
you can use the "OFFSET" keyword:
'''

cursor.execute('SELECT * FROM customers LIMIT 5 OFFSET 2')
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")

# 9- Python MySQL Join
# Join Two or More Tables

'''
You can combine rows from two or more tables, based on a related
column between them,
by using a JOIN statement.
Consider you have a "users" table and a "products" table:
'''
tb_exist = check_table_exists('products')
if tb_exist :
    cursor.execute('DROP TABLE products')
    cursor.execute('CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')
else:
    cursor.execute('CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')

sql = 'INSERT INTO products (name) VALUES(%s)'
val = [
    ('BIOS Battery',),
    ('CPU Intel I7-HQ',),
    ('VGA Card Nvidia G8090',),
    ('Mother Board Asus',),
    ('Monitor 34" wide Asus',),
    ('Power Green',),
    ('Mouse Wireless Rapo',)
    ]
cursor.executemany(sql, val)
mydb.commit()
print(cursor.rowcount, 'Record Was Inserted Into product Table.')
print("--------------------")


tb_exist = check_table_exists('users')
if not tb_exist :
    cursor.execute('CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), password VARCHAR(50), email VARCHAR(255),fav INT, FOREIGN KEY (fav) REFERENCES products(id))')


sql = 'INSERT INTO users (name, password, email, fav) VALUES(%s, %s, %s, %s)'
val = [
    ('Hamed', 123, 'abcd@test.com', 1),
    ('Mohammad', 123, 'abcd@test.com', 1),
    ('Mahdi', 123, 'abcd@test.com', 2),
    ('Hosein', 123, 'abcd@test.com', 3),
    ('Ali', 123, 'abcd@test.com', 2),
    ('Reza', 123, 'abcd@test.com', 4),
    ('Sadegh', 123, 'abcd@test.com', 1)
    ]
cursor.executemany(sql, val)
mydb.commit()
print(cursor.rowcount, 'Record Was Inserted Into users Table.')
print("--------------------")

'''
These two tables can be combined using users' fav field and 
products' id field.
'''

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")

'''
Note: You can use JOIN instead of INNER JOIN. They will both
give you the same result.
'''

# LEFT JOIN
'''
In the example above, Hamed, Mohammad, Mahdi, Hosein, Ali, Reza,
and Sadegh were excluded from the result, that is because INNER
JOIN only shows the records where there is a match.

If you want to show all users, even if they do not have a favorite
product, use the LEFT JOIN statement:
'''

sql = "SELECT " \
"users.name AS user, " \
"products.name AS favorite " \
"FROM users " \
"LEFT JOIN products ON users.fav = products.id"

cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")

# RIGHT JOIN
'''
If you want to return all products, and the users who have them
as their favorite, even if no user have them as their favorite,
use the RIGHT JOIN statement:
'''

sql = "SELECT " \
"users.name AS user, " \
"products.name AS favorite " \
"FROM users " \
"RIGHT JOIN products ON users.fav = products.id"

cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)
print("--------------------")

'''
Note: Monitor, Power, and Mouse which have no users products, are not
included in the result.
'''
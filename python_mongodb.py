# Python MongoDB
'''
Python can be used in database applications.
One of the most popular NoSQL database is MongoDB.
'''
# MongoDB
'''
MongoDB stores data in JSON-like documents, which makes the
database very flexible and scalable.

To be able to experiment with the code examples in this tutorial,
you will need access to a MongoDB database.
'''
# you can download a free MongoDB database at https://mongodb.com.
# Or get started right away with a MongoDB cloud service at
# https://www.mongodb.com/cloud/atlas.
# 

# PyMongo

# Python needs a MongoDB driver to access the MongoDB database.
# In this tutorial we will use the MongoDB driver "PyMongo".
# We recommend that you use PIP to Install "PyMongo".
# PIP is most likely already installed in your Python environment.
# Navigate your command line to the location of PIP, and type the
# following:
# C:\Users\YourName\AppData\Local\Programs\Python\Python314\Scripts>python -m pip install pymongo
# Now you have downloaded and installed a mongoDB driver.

# Test PyMongo
'''
To test if the installation was successful, or if you already have
"pymongo" installed, create a Python page with the following content:
'''

import pymongo

'''
If the above code was executed with no errors, "pymongo" is
installed and ready to be used.
'''

# Python MongoDB Create Database
# Creating a Database
'''
To create a database in MongoDB, start by creating a MongoClient
object, then specify a connection URL with the correct ip address
and the name of the database you want to create.
MongoDB will create the database if it does not exist, and make
a connection to it.
'''

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['pytestdb']

'''
Important: In MongoDB, a database is not created until it gets
content!

MongoDB waits until you have created a collection (table), with
at least one document (record) before it actually creates the 
database (and collection).
'''
# Check if Database Exists
'''
Remember: In MongoDB, a database is not created until it gets 
content, so if this is your first time creating a database,
you should complete the next two chapters (create collection
and create document) before you check if the database exists!
'''

print(client.list_database_names())

'''Or you can check a specific database by name:'''

dblist = client.list_database_names()
if 'pytestdb' in dblist:
    print('the database exists.')
print('------------------------------')

# Python MongoDB Create Collection
# Creating a Collection

'''
A collection in MongoDB is the same as a table in SQL databases.
To create a collection in MongoDB, use database object and specify
the name of the collection you want to create.

MongoDB will create the collection if it does not exist.
'''

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['pytestdb']
collection = db['customers']

'''
Important: In MongoDB, a collection is not created until it gets
content!

MongoDB waits until you have inserted a document before it actually
creates the collection.
'''

# Check if Collection Exists

'''
Remember: In MongoDB, a collection is not created until it gets
content, so if this is your first time creating a collection,
you should complete the next chapter (create document) before
you check if the collection exists!

You can check if a collection exist in a database by listing all
collections:
'''

print(db.list_collection_names())
print('------------------------------')

'''Or you can check a specific collection by name:'''
collist = db.list_collection_names()
if 'customers' in collist:
    print('The collection exists.')
print('------------------------------')

# Python MongoDB Insert Document
'''
A document in MongoDB is the same as a record in SQL databases.
'''
# Insert Into Collection
'''
To insert a record, or document as it is called in MongoDB, into a 
collection, we use the insert_one() method.

The first parameter of the insert_one() method is a dictionary containing
the name(s) and value(s) of each field in the document you want to insert.
'''
import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['pytestdb']
collection = db['customers']
record = {'name': 'Hamed', 'city' : 'Tehran'}
insert = collection.insert_one(record)

# Return the _id field

'''
The insert_one() method returns a InsertOneResult object, which has a 
property, inserted_id, that holds the id of the inserted document.

Insert another record in the 'customers' collection, and return the value
of the _id field:
'''

record = {'name': 'Ali', 'city': 'Najaf'}
insert = collection.insert_one(record)
print(insert.inserted_id)
print('------------------------------')

'''
If you do not specify _id field, then MongoDB will add one for you and
assign a uniqe id for each document.

In the example above no _id field was specified, so MongoDB assigned a 
unique _id for the record (document).
'''

# Insert Multiple Documents

'''
To insert multiple document into a collection in MongoDB, we use the 
insert_many() method.
The first parameter of the insert_many() method is a list containing
dictionaries with the data you want to insert:
'''
collection.drop()

import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
database = client['pytestdb']
collection = database['customers']
customers_list = [
    {'name':'Mohammad', 'city':'Tehran'},
    {'name':'Ali', 'city':'Khorasan Razavi'},
    {'name':'Hamed', 'city':'Qom'},
    {'name':'Rasoul', 'city':'Kermanshah'},
    {'name':'Javad', 'city':'Zanjan'},
    {'name':'Hojat', 'city':'Ardebil'},
    {'name':'Abolfazl', 'city':'Mazandaran'},
    {'name':'Komeil', 'city':'Hormozghan'},
    {'name':'Malek', 'city':'Ahvaz'},
    {'name':'Meysam', 'city':'Kordestan'},
    {'name':'Hassan', 'city':'Karaj'},
    {'name':'Masoud', 'city':'Tehran'},
    {'name':'Sajad', 'city':'Qom'},
    {'name':'Mojtaba', 'city':'Tehran'},
]

insert = collection.insert_many(customers_list)
print(insert.inserted_ids)
print('------------------------------')

'''
The insert_many() method returns a InsertManyResult object, which has a
property, inserted_ids, that holds the ids of the inserted documents.
'''

# Insert Multiple Documents, with Specified IDs
'''
If you do not want MongoDB to assign unique ids for your document, you
can specify the _id field when you insert the document(s).

Remember that the value has to be unique. Two documents cannot have the
same _id.
'''

collection.drop()

client = pymongo.MongoClient('mongodb://localhost:27017/')
database = client['pytestdb']
collection = database['customers']
customers_list = [
    {'_id':1, 'name':'Ali', 'city':'Isfahan'},
    {'_id':2, 'name':'Komeil', 'city':'Ardebil'},
    {'_id':3, 'name':'Malek', 'city':'Kerman'},
    {'_id':4, 'name':'Ammar', 'city':'Qom'},
    {'_id':5, 'name':'Hamed', 'city':'Tehran'},
    {'_id':6, 'name':'Karim', 'city':'Qom'},
    {'_id':7, 'name':'Ebrahim', 'city':'Tehran'},
    {'_id':8, 'name':'Ehsan', 'city':'Tabriz'}
]
insert = collection.insert_many(customers_list)
print(insert.inserted_ids)
print('------------------------------')

# Python MongoDB Find
'''
In MongoDB we use the find() and find_one() methods to find data in a
collection.
Just like the SELECT statement is used to find data in a table in a MySQL
database.
'''

# Find One
'''
To select data from a collection in MongoDB, we can use the find_one() method.
The find_one() method returns the first occurrence in the selection.
'''

finded_item = collection.find_one()
print(finded_item)
print('------------------------------')

# Find All
'''
To select data from a table in MongoDB, we can also use the find() method.
The find() method returns all occurrences in the selection.
The first parameter of the find() method is a query object. In this example
we use an empty query object, which selects all documents in the collection.

No parameters in the find() method gives you the same result as SELECT *
in MySQL.
'''

collection = database['customers']
for item in collection.find():
    print(item)
print('------------------------------')

# Return Only Some Fields
'''
The second parameter of the find() method is an object describing which
fields to include in the result.

This parameter is optional, and if omitted, all fields will be included
in the result.
'''

collection = database['customers']
for item in collection.find({},{'_id':0, 'name':1, 'city':1}):
    print(item)
print('------------------------------')

'''
You are not allowed to specify both 0 and 1 values in the same object
(exept if one of the fields is the _id field). If you specify a field with
the value 0, all other fields get the value 1, and vice versa:
This example will exclude 'address' from the result:
'''
for item in collection.find({}, {'city':0}):
    print(item)
print('------------------------------')

'''
You get an error if you specify both 0 and 1 values in the same object
(exept if one of the fields is the _id field):
'''

for item in collection.find({}, {'_id':0, 'name':1}):
    print(item)
print('------------------------------')

# Python MongoDB Query
# Filter the Result
'''
When finding documents in a collection, you can filter the result by
using a query object.
The first argument of the find() method is a query object, and is used
to limit the search.
'''

query = {'city':'Tehran'}
documents = collection.find(query)
for item in documents:
    print(item)
print('------------------------------')

# Advanced Query
'''
To make advanced queries you can use modifiers as values in the query object.
E.g. to find the documents where the 'city' field starts with the letter
'S' or higher(alphabetically), use the greater than modifier:{'$gt':'S'}:
'''

query = {'city': {'$gt': 'T'}}
documents = collection.find(query)
for item in documents:
    print(item)
print('------------------------------')

# Filter With Regular Expressions
'''
You can also use regular expressions as a modifier.
Regular expressions can only be used to query strings.

To find only the documents where the 'city' field starts with the letter
'T', use the regular expression {'$regex': '^T'}:
'''
# Start with T 
query = {'city': {'$regex': '^T'}}
documents = collection.find(query)
for item in documents:
    print(item)
print('------------------------------')

# End with an
query = {'city': {'$regex': 'an$'}}
documents = collection.find(query)
for item in documents:
    print(item)
print('------------------------------')

# Words contain e letter after first letter and before last letter

query = {'city': {'$regex': '.e.'}}
documents = collection.find(query)
for item in documents:
    print(item)
print('------------------------------')

# Python MongoDB Sort
# sort the Result
'''
Use the sort() method to sort the result in ascending or descending order.

The sort() method takes one parameter for 'fieldname' and one parameter
for 'direction' (ascending is the default direction).
'''

documents = collection.find().sort('name')
for item in documents:
    print(item)
print('------------------------------')

# Sort Descending
'''
Use the value -1 as the second parameter to sort descending.
sort('name',1) # ascending
sort('name',-1) # descending
'''

documents = collection.find().sort('name', -1)
for item in documents:
    print(item)
print('------------------------------')

# Python MongoDB Delete Document
# Delete Document

'''
To delete on document, we use the delete_one() method.
The first parameter of the delete_one() method is a query object
defining which document to delete.

Note: If the query finds more than one document, only the first 
occurrence is deleted.
'''
query = {'name':'Hamed', 'city':'Tehran'}
collection.delete_one(query)
for item in collection.find():
    print(item)
print('------------------------------')

# Delete Many Documents
'''
To delete more than one document, use the delete_many() method.
The first parameter of the delete_many() method is a query object
defining which documents to delete.
'''

query = {'city': {'$regex': '^T'}}
deleted_items = collection.delete_many(query)
print(deleted_items.deleted_count, 'documents deleted.')
print('------------------------------')

# Delete All Documents in a Collection
'''
To delete all documents in a collection, pass an empty query object to 
the delete_many() method:
'''

deleted_items = collection.delete_many({})
print(deleted_items.deleted_count, 'documents deleted.')
print('------------------------------')

# Python MongoDB Drop Collection
# Delete Collection

'''
You can delete a table, or collection as it is called in MongoDB, by using
the drop() method.
'''
databases = database.list_collection_names()
collection = database['users']
if 'users' in databases:
    collection.drop()

users_list = [
    {'_id':1, 'name':'hamed', 'email':'abc@email.ir'},
    {'_id':2, 'name':'danial', 'email':'abc@email.ir'},
    {'_id':3, 'name':'emran', 'email':'abc@email.ir'},
    {'_id':4, 'name':'zakaria', 'email':'abc@email.ir'}
]

insert = collection.insert_many(users_list)
print(insert.inserted_ids, 'users added.')
print('------------------------------')

# collection.drop()
# print('users collection deleted.')
# print('------------------------------')

'''
The drop() method returns true if the collection was dropped successfully,
and false if the collection does not exist.
'''

# Python MongoDB Update
# Update Collection

'''
You can update a record, or document as it is called in MongoDB,
by using the update_one() method.
The first parameter of the update_one() method is a query object
defining which document to update.
Note: If the query finds more than one record, only the first
occurrence is updated.
The second parameter is an object defining the new values of the 
document.
'''

query = {'_id':1, 'name':'hamed', 'email':'abc@email.com'}
new_value = {'$set':{'_id':1, 'name':'Ali', 'email':'abc@email.com'}}

collection = database['users']
collection.update_one(query, new_value)

for item in collection.find():
    print(item)
print('------------------------------')

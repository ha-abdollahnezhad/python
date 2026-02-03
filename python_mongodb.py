# # Python MongoDB
# '''
# Python can be used in database applications.
# One of the most popular NoSQL database is MongoDB.
# '''
# # MongoDB
# '''
# MongoDB stores data in JSON-like documents, which makes the
# database very flexible and scalable.

# To be able to experiment with the code examples in this tutorial,
# you will need access to a MongoDB database.

# you can download a free MongoDB database at https://mongodb.com.
# Or get started right away with a MongoDB cloud service at
# https://www.mongodb.com/cloud/atlas.
# '''
# # PyMongo
# '''
# Python needs a MongoDB driver to access the MongoDB database.
# In this tutorial we will use the MongoDB driver "PyMongo".
# We recommend that you use PIP to Install "PyMongo".
# PIP is most likely already installed in your Python environment.
# Navigate your command line to the location of PIP, and type the
# following:
# C:\Users\YourName\AppData\Local\Programs\Python\Python314\Scripts>python -m pip install pymongo
# Now you have downloaded and installed a mongoDB driver.
# '''
# # Test PyMongo
# '''
# To test if the installation was successful, or if you already have
# "pymongo" installed, create a Python page with the following content:
# '''

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

'''Or you can check a specific collection by name:'''
collist = db.list_collection_names()
if 'customers' in collist:
    print('The collection exists.')
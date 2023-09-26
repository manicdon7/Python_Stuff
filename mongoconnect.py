import pymongo

# MongoDB connection parameters
mongodb_host = 'mongodb+srv://manikandan05082003:Manicdon07%40@cluster0.scriurb.mongodb.net/'  # Replace with your MongoDB server host
mongodb_port = 3001       # Replace with your MongoDB server port
database_name = 'hey'     # Replace with the name of your database

# Initialize a MongoDB client
client = pymongo.MongoClient(mongodb_host, mongodb_port)

# Access your database
db = client[database_name]

# Access a specific collection (equivalent to a table in SQL databases)
collection = db['mongo']  # Replace with the name of your collection

# Insert a document into the collection
data = {
    'title': 'Sample Document',
    'content': 'This is a sample document for MongoDB connection.'
}
inserted_document = collection.insert_one(data)
print(f'Inserted document ID: {inserted_document.inserted_id}')

# Find a document in the collection
found_document = collection.find_one({'title': 'Sample Document'})
print('Found document:')
print(found_document)

# Update a document in the collection
update_query = {'title': 'Sample Document'}
update_data = {'$set': {'content': 'Updated content'}}
collection.update_one(update_query, update_data)

# Find the updated document
updated_document = collection.find_one({'title': 'Sample Document'})
print('Updated document:')
print(updated_document)

# Delete the document
# delete_query = {'title': 'Sample Document'}
# collection.delete_one(delete_query)

# Close the MongoDB connection
client.close()

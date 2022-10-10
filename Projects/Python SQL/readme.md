This is a project to demonstrate the connectivity of python to three types of databases:
**RDBMS,NOSQL and Cloud***.

For RDBMS I have created a MySQL server on google colab and implemented a Book Database to demonstrate few basic CRUD operations(read,delete etc.). I have 
used mysql-python-connector for the database connectivity.

For NoSQL I have created a MongoDb server on colab and used an existing csv file(listings.csv) to create a database and demonstrated the document approach 
of the MongoDB. I used pymongo connector for the database connectivity.

I had created an Azure DB prior to the execution of the code for Cloud DB connectivity using odbc(open database connectivity) connector. However I 
had to delete the database in order to avoid expenses since Azure SQL database is not free. Thus the cloud database connectivity cell does not work since 
the database does not exist! I included it so that one can understand how to connect to a cloud database using python.

We need to just run the colab file. The python code automatically fetches the data.

The other colab file Shopify.ipynb is another file containing SQL commands that I developed while attempting to get into the 
Shopify Internship.

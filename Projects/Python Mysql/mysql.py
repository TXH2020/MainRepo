import mysql.connector as my
try:
 cnx=my.connect(user="root",
                host="localhost",password="<your password>",database="python_mysql")
except my.Error as e:
 print(e)
else:
 cr=cnx.cursor()
 print("******************")

 cr.execute("Select *from books")    #Manipulate database
 k=0
 for i in cr:
     k=k+1
     print(i)
 print("No. of records=", k)
 print("******************")

 cr.execute("show columns from books")
 for i in cr:
     print(i[0])                         #Showing column names
 print("******************")

 add_book = ("INSERT INTO books"
                 "(id, title, isbn)"
                 "VALUES (%s, %s, %s)")
 book = (86,'Hello World',"1234567898784")
 cr.execute(add_book,book)            #Inserting record
 cr.execute("select *from books")
 k=0
 for i in cr:
     k = k + 1
 print("Number of records after inserting is=",k)
 print("*******************")

 cnx.close()

 #Like this we can use any Mysql command in Python using mysql connector.
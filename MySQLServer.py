import mysql.connector
from mysql.connector import error

try:
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="#123456#"
		database="alx_book_store"
		)
	if mydb.is_connected()
		mycursor = mydb.cursor()
		mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
		print("Database 'alx_book_store' created successfully!")

except Error as e:
	print(f"Error connecting to MySQL: {e}")
finally:
	if mydb.is_connected():
		mycursor.close()
		mydb.close()

import mysql.connector
database= mysql.connector.connect(
	host='localhost',
	user='root',)
cursorObject = database.cursor()
cursorObject.execute("create database test1")
print("All done")
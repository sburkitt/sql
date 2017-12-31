# CSV import
import csv 
import sqlite3

with sqlite3.connect("csv.db") as connection:
	c = connection.cursor()

	#open CSV 
	employees = csv.reader(open("employees.csv",'rU'))

	#new table
	c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

	#data in 
	c.executemany("INSERT INTO employees(firstname, lastname) values (?,?)", employees)

connection.close()
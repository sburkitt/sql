#SQLITE Stuff 
import sqlite3 

##new connection 
with sqlite3.connect('new.db') as conn:

	#cursor 
	c = conn.cursor()

	#c.execute("DROP TABLE IF EXISTS population")

	#create tabless
	#c.execute("""CREATE TABLE population
		#(city TEXT, state TEXT, population INT)
		#""")

	#inserting data
	#c.execute("INSERT INTO population VALUES('New York City', 'NY', 8400000)")
	#c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

	cities = [
	('Boston', 'MA', 600000),
	('Chicago', "IL", 2700000),
	('Houston', 'TX', 2100000),
	('Phoenix', 'AZ', 1500000),
	]

	c.executemany('INSERT INTO population VALUES(?,?,?)',cities)




#close connection
conn.close()
#SQLITE Stuff 
import sqlite3 

##new connection 
with sqlite3.connect('new.db') as conn:

	#cursor 
	c = conn.cursor()

	c.execute("DROP TABLE IF EXISTS population")

	#create tabless
	c.execute("""CREATE TABLE population
		(city TEXT, state TEXT, population INT)
		""")

	#inserting data
	#c.execute("INSERT INTO population VALUES('New York City', 'NY', 8400000)")
	#c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

	cities = [
	('Boston', 'MA', 600000),
	('Los Angeles', 'CA', 38000000),
	('Philadelphia', 'PA', 1500000),
	('San Antonio', 'TX', 1400000),
	('San Diego', 'CA', 130000),
	('Chicago', "IL", 2700000),
	('Dallas', 'TX', 1200000),
	('Houston', 'TX', 2100000),
	('Phoenix', 'AZ', 1500000),
	('San Jose', 'CA', 900000),
	('Jacksonville', 'FL', 800000),
	('Indianapolis', 'IN', 800000),
	('Austin', 'TX', 80000),
	('Detroit', 'MI', 700000),
	]

	#Error handling (say wrong table)

	try:

		c.executemany('INSERT INTO population VALUES(?,?,?)',cities)
		c.execute("SELECT * FROM population WHERE population > 1000000")

	except sqlite3.OperationalError: 
		print("oops! something went wrong")

rows = c.fetchall()

for r in rows:
	print(r[0], r[1], r[2])




#close connection
conn.close()
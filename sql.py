#SQLITE Stuff 
import sqlite3 

##new connection 
conn = sqlite3.connect("new.db")

#cursor 
c = conn.cursor()

#create tables 
#c.execute("""CREATE TABLE population
	#(city TEXT, state TEXT, population INT)
	#""")

#inserting data
c.execute("INSERT INTO population VALUES('New York City','NY', 8400000)")
c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

#close connection
conn.close()
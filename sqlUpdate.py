import MySQLdb

#Open database connection
db =  MySQLdb.connect (host="localhost",user="user",passwd="password",db="school")

#prep a cursor object using cursor() method; cursor is like a navigation method
db.autocommit(True)
cursor = db.cursor(MySQLdb.cursors.DictCursor)

name='derek'
age=12
gradeLevel=10

sql = "UPDATE students SET age=16 WHERE name='derek'"
cursor.execute(sql)

cursor.close()
db.close()

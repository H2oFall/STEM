import MySQLdb
db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="students")

#create cursor
cur = db.cursor(MySQLdb.cursors.DictCursor)

#create table
sql = "SELECT * from students"

cur.execute(sql)

rows = cur.fetchall()
for row in rows:
	print("name: " + str(row['name']) + " age: " + str(row['age']) + " GradeLevel: " + str(row['gradeLevel']))

#disconnect
cur.close()
db.close()
	

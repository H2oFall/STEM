import MySQLdb
db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="students")

#create cursor
cur = db.cursor(MySQLdb.cursors.DictCursor)

name = 'stephen'
age = 7
gradeLevel = 11

#create table
sql = "INSERT INTO `students` (`name`, `age`, `gradeLevel`) VALUES ('sam', '10', '5');"

cur.execute(sql)

rows = cur.fetchall()
for row in rows:
	print("name: " + str(row['name']) + " age: " + str(row['age']) + " GradeLevel: " + str(row['gradeLevel']))

#disconnect
cur.close()
db.close()

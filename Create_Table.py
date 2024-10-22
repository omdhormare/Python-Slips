import mysql.connector as mc
con=mc.connect(host="localhost",password="root",username="root",database="collage")

db=con.cursor()

db.execute("create table collage(cno INT PRIMARY KEY,cname varchar(20),address varchar(20))")
#db.execute("drop table collage")
print("Succefully Create Table...")
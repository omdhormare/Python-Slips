import mysql.connector as mc

con=mc.connect(host="localhost",password="root",username="root",database="collage")

db=con.cursor()
db.execute("insert into collage values(3,'VJIT','pune')")

con.commit()

print("insert values..")
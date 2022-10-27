

import mariadb

print("hoi")

mydb = mariadb.connect(
  host="localhost",  #port erbij indien mac
  user="root",
  password="",
  database="flaviadb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sport")

myresult = mycursor.fetchall() # om de records naar toe te trekken

print(myresult)
for i in myresult:
	print (i[2])
	if i[2] =='football':
		print("il calcio e'brutto")

woord1= int(input("hoe oud ben je "))
woord2 =int(input('hoe oud is je hond? '))
print(woord1 + woord2)

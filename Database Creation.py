import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="cnet"
)

mycursor = mydb.cursor()

# db named cnet is here
mycursor.execute("CREATE DATABASE cnet")

mycursor.execute("CREATE TABLE Chat (id int NOT NULL AUTO_INCREMENT PRIMARY KEY,user VARCHAR(100), message VARCHAR(255))")
#table named chat is here with two columns namely user and the message

sql = "INSERT INTO chat (user, message) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM chat")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


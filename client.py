import socket
import threading
import time
#db config
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="cnet"
)

mycursor = mydb.cursor()


tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data))
        except:
            pass
        finally:
            tLock.release()

host = '127.0.0.1'
port = 0

server = ('127.0.0.1',5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

alias = input("Name: ")
mycursor.execute("SELECT * FROM chat where user= '%s'" % alias)

myresult = mycursor.fetchall()
try:
    for result in myresult:
        print(result)
except:
    print("New User")

message = input(alias + "-> ")
while message != 'q':
    if message != '':
        s.sendto(bytes(alias + ": " + message, 'utf-8'), server)
        sql = "INSERT INTO chat (user, message) VALUES (%s, %s)"
        val = (alias, message)
        mycursor.execute(sql, val)
        mydb.commit()

    tLock.acquire()
    message = input(alias + "-> ")
    tLock.release()
    time.sleep(0.2)

shudown = True
rT.join()
s.close()

import socket
import threading
import time
#db config
import mysql.connector                
mydb = mysql.connector.connect(   #db connection
  host="localhost",
  user="root",
  database="cnet"
)
mycursor = mydb.cursor()


tLock = threading.Lock()      #multithreading lock for avoiding race cond
shutdown = False

def receving(name, sock):    #function for recieving messages
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data))
        except:
            pass
        finally:
            tLock.release() #multithreading lock for avoiding race cond
''' for diff comm communication
host = '127.168.10.7'
port = 4005
server = ('127.168.10.10',4000)
''' #ends here

host = '127.0.0.1'
port = 5005 # Port assigned after the range of reserved ports i.e. 1025

server = ('127.0.0.1',5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

alias = input("Name: ")
mycursor.execute("SELECT * FROM chat where user= '%s'" % alias) #querry for fetching all records of a user

myresult = mycursor.fetchall()
try:
    for result in myresult:
        print(result)
except:
    print("New User")

message = input(alias + "-> ")
while message != 'q':   #loop untill user quits
    if message != '':
        s.sendto(bytes(alias + ": " + message, 'utf-8'), server)
        sql = "INSERT INTO chat (user, message) VALUES (%s, %s)"
        val = (alias, message)
        mycursor.execute(sql, val)
        mydb.commit()

    tLock.acquire() #threading for avoiding race condition between differnt users texting at same time
    message = input(alias + "-> ")
    if message =='f':
        filesignal='f'
        filename= input(str("please enter the file name of file : "))
        file = open(filename, 'rb')
        
        file_data=file.read(1024)
        print(str(file_data))
        s.sendto(bytes(filesignal+str(file_data), 'utf-8'), server)
        
        #s.sendto(bytes(file_data),server)
        print("Data has been transmitted successfully")
    tLock.release()
    time.sleep(0.2)

shudown = True
rT.join()
s.close()

import socket
import time
#db config
'''
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="cnet"
)

mycursor = mydb.cursor()
#db
'''

#filename=input(str("please enter the file name for incoming file : "))
''' for diggernt computer communication
host = '192.168.10.7' #Server ip
port = 4000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((host, port))
''' #differnt comm ends here
 for same pc communication
host = '127.0.0.1' # <a class="zem_slink" title="Localhost" href="http://en.wikipedia.org/wiki/Localhost" rel="wikipedia">Loopback address</a> for the port
port = 5000 # Port assigned after the range of reserved ports i.e. 1025

clients = [] # Now clients can be many, so this list maintains the clients.

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Using <a class="zem_slink" title="User Datagram Protocol" href="http://en.wikipedia.org/wiki/User_Datagram_Protocol" rel="wikipedia">UDP</a> protocol
serverSocket.bind((host,port))
serverSocket.setblocking(0)

quitting = False
print("Server Started.")
while not quitting:
    try:
        data, addr = serverSocket.recvfrom(1024) # Here, 1024 is the buffer, which can be set to any value
        print(str(data))
        if 'f' in str(data[0:1]):
            print("something")
            file= open("filenamerecv.txt",'wb')
            file.write(data)
            file.close()

        if "Quit" in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)

        
        print(time.ctime(time.time()) + str(addr) + ": :" + str(data)) # Printing <a class="zem_slink" title="Timestamp" href="http://en.wikipedia.org/wiki/Timestamp" rel="wikipedia">Time stamp</a> of messages from each client.
        for client in clients:
            serverSocket.sendto(data, client)
    except:
        pass

'''
sql = "INSERT INTO chat (user, message) VALUES (%s, %s)"
val = (str(addtr), str(data))
mycursor.execute(sql, val)
mydb.commit()
   '''             
                
    
serverSocket.close()

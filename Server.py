import socket
serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #To create a new socket object
import threading                                      #To make multiple clients connect simultaneously
host=socket.gethostname()                             #To get the server's hostname
port=12345                                            #To identify port for the server
serv_add=(host,port)                                  #To store the host and port in a tuple as server address
serv.bind(serv_add)                                   #To bind the server to the specified host and port
serv.listen()                                         #Waiting for clients to connect.....
members=[]                                            #To store all connected client sockets
usernames=[]                                          #To store the usernames of connected clients

### We built this function to send messages to all clients in the chatroom ###
def broadcast(tosend):
    for mb in members:                                #To loop over each connected client
        mb.send(tosend.encode())                      #To Send the message to that client
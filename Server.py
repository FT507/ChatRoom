import socket
serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
import threading                                      #To make multiple clients connect simultaneously
host=socket.gethostname()
port=12345
serv_add=(host,port)
serv.bind(serv_add)
serv.listen(10)
members=[]
usernames=[]

### We built this function to send messages to all clients in the chatroom ###
def broadcast(sendmsg):
    for mb in members:
        mb.send(sendmsg.encode())


#Receive message for client , detect connection failed , target for threading
def receive(member):
    #Remeber we implement IN_LOOP as receiving not called for on time and broke it in case of fail in connection
    while True:
        try:
            msg = member.recv(1024)
            broadcast(msg.decode())
        except:
            print("ERROR 404")
            Index = members.index(member)
            username = usernames[Index]
            member.recv(1024)
            broadcast(username + "IS REMOVED")
            usernames.remove(username)
        break


## Created to start threading between client and server
def start():
    member , addr  = serv.accept()
    member.send("NICKNAMES".encode())
    userNames = member.recv(1024).decode()
    ## add more member without effecting on older ones
    userNames.append(userNames)
    members.append(members)
    broadcast(userNames)
    thread = threading.Thread(target=receive,args=(userNames,))  #The target is receive() function to get messages simultaneously
    thread.start()
    print("Server is waiting")

start()

 # def server():


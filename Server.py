import socket
serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
import threading                                         #To make multiple clients connect simultaneously
host=socket.gethostname()
port=12344
serv_add=(host,port)
serv.bind(serv_add)
serv.listen()
Members=[]
UserNames=[]

### We built this function to send messages to all clients in the chatroom ###
def broadcast_message(sendmsg, member):
    From = UserNames[Members.index(member)]
    for mb in Members:
        if mb != member:
            mb.sendall("{}: {}".format(From,sendmsg).encode())
        else:
            mb.sendall("You: {}".format(sendmsg).encode())

def broadcast(sendmsg):
    for mb in Members:
        mb.send(sendmsg.encode())
#Receive message for client , detect connection failed , target for threading
def receive(member):
    #Remeber we implement IN_LOOP as receiving not called for on time and broke it in case of fail in connection
    while True:
        try:
            msg = member.recv(1024).decode()
            broadcast_message(msg, member)
        except:
            print("ERROR 404")
            Index = Members.index(member)
            username = UserNames[Index]
            broadcast(username + " IS REMOVED")
            UserNames.remove(username)
            Members.remove(member)
            member.close()
            break


## Created to start threading between client and server
def start():
    while True:
        member , addr  = serv.accept()
        member.send("NICKNAME".encode())
        username = member.recv(1024).decode()
        ## add more member without effecting on older oness
        UserNames.append(username)
        Members.append(member)
        broadcast("  **" + username + " joined the chatroom**")
        thread = threading.Thread(target=receive,args=(member, ))  #The target is receive() function to get messages simultaneously
        thread.start()

print("Server is waiting")
start()

 # def server():


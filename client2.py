import threading
import socket
NICKNAME = input('Choose an Nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 12344))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "NICKNAME":
                client.send(NICKNAME.encode('ascii'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break

def client_send():
    while True:
        try:
            message= '{}:{}'.format(NICKNAME,input(" "))
            client.sendall(message.encode('ascii'))
            #print("send correctly")
        except:
            print("Error")

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
send_thread=threading.Thread(target=client_send)
send_thread.start()
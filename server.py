import socket
from threading import Thread

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip="127.0.0.1"
port=8000
clientsList=[]
nicknameList=[]

server.bind((ip,port))
server.listen()

def remove(con):
    if con in clientsList:
        clientsList.remove(con)

def removenick(nickname):
    if nickname in nicknameList:
        nicknameList.remove(nickname)

print("Server connected")
def broadcastm(msg,con):
    for client in clientsList:
        if client!= con:
            try:
                client.send(msg.encode("utf-8"))
            except:
                remove(client)


def clientThread(con,nickname):
    con.send("Welcome to the chat!".encode("utf-8"))
    while True:
        try:
            messages=con.recv((2048).decode("utf-8"))
            if messages:
                messagetosend="<"+nickname + ">" +messages
                broadcastm(messagetosend,con)
            else:
                remove(con)
                removenick(nickname)
        except:
            continue
        

while True:
    con,address=server.accept()
    clientsList.append(con)
    con.send("NICKNAME".encode("utf-8"))
    nickname=con.recv((2048).decode("utf-8"))
    nicknameList.append(nickname)
    message="{} has joined".format(nickname)
    broadcastm(message,con)
    newthread=Thread(target=clientThread,args=(con,nickname))
    newthread.start()



    

    

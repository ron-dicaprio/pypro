#-*- coding:utf-8 -*-
#!/usr/bin/env python
import socket,threading
host='127.0.0.1'
port=10240
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定地址
server.bind((host,port))

# 监听20个客户端请求
server.listen(20)
print(f'[*]start listening on {host}:{port}[*]')

def handle(self):
    clientinfo=self.recv(1024)
    toclientmsg='server:'+bytes.decode(clientinfo)
    self.sendall(toclientmsg.encode())
    self.close()


#Function that continuosly searches for connections
def handle(connectionList, addressList):
    for j in range(0,Conn):
        message = connectionList[j].recv(1024)
        print(message)
        #for loop to send message to each
        for i in range(0,Conn):
            connectionList[i].sendto(message, addressList[i])

#Name of list used for connections
addressList = []
connectionList = []
Conn = 0
while True:
    client,addr=server.accept()
    addressList.append((addr))
    connectionList.append((client))
    Conn=Conn+1
    client_thred=threading.Thread(target=handle,args=(connectionList, addressList))
    client_thred.start()


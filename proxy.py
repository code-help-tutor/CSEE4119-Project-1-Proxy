WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/usr/bin/env python3.10
import socket
import sys
from socket import *


def client2proxy2server(listenPort, fakeIP, serverIP):
    while True:
        try:
            # Start proxying
            # Create socket from proxy to server
            # Declare the fixed server port
            serverPort = 8080
            proxy2serverSocket = socket(AF_INET, SOCK_STREAM)
            proxy2serverSocket.bind((fakeIP, 0))
            proxy2serverSocket.connect((serverIP, serverPort))
            # print('From proxy: Connected to the server')

            # Create socket from client to proxy
            # client2proxySocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            client2proxySocket = socket(AF_INET, SOCK_STREAM)
            client2proxySocket.bind(('', listenPort))
            client2proxySocket.listen(1)
            # print('From proxy: Waiting for the new client connection')
            client_connectionSocket, addr = client2proxySocket.accept()
            # print('From proxy: Connected to the client')
            isExit = False
            while not isExit:
                # print("From proxy: Waiting message from client...")
                # Receive the message from client machine
                clientMessage = ''
                isContinue = True

                # Detect the newline code \n 10.13
                while isContinue:
                    clientMessage_tmp = client_connectionSocket.recv(2048).decode()
                    clientMessage += clientMessage_tmp
                    # Check the status of the client socket
                    if not clientMessage:
                        isExit = True
                        # print("From client: connection closed")
                        # client_closed = "The client closed connection"
                        # proxy2serverSocket.send(client_closed.encode())
                        isContinue = False
                    # Finish
                    if b'\n' in clientMessage.encode():
                        isContinue = False
                        clientMessage_tmp = ''
                # Finish

                if not isExit:
                    # Send the client message to server
                    # print("From client: " + clientMessage)
                    proxy2serverSocket.sendall(clientMessage.encode())
                    # print("From proxy: Sent client message to server!")
                    # Receive the message from server
                    # print("From proxy: Waiting message from server...")
                    serverMessage = ''
                    isContinue = True

                    # Detect the newline code \n 10.13
                    while isContinue:
                        serverMessage_tmp = proxy2serverSocket.recv(2048).decode()
                        serverMessage += serverMessage_tmp
                        if not serverMessage:
                            # print('From server: connection closed')
                            # server_closed = "The server closed connection"
                            # client_connectionSocket.send(server_closed.encode())
                            isExit = True
                            isContinue = False
                        if b'\n' in serverMessage.encode():
                            isContinue = False
                            serverMessage_tmp = ''
                    # Finish

                if not isExit:
                    # Send server message to client machine
                    client_connectionSocket.sendall(serverMessage.encode())
                    # print("From proxy: Sent server message to client!")
                    # print("From proxy: Waiting message from client...")
                if isExit:
                    try:
                        client_connectionSocket, addr = client2proxySocket.accept()
                        isExit = False
                    except client2proxySocket.timeout:
                        isExit = True
            # Close sockets
            proxy2serverSocket.close()
            client2proxySocket.close()
            client_connectionSocket.close()
            # print("From Proxy: Socket for both client and server are closed")
        except KeyboardInterrupt:
            # print("From proxy: Ctrl+C detected, closing the socket...")
            proxy2serverSocket.close()
            client2proxySocket.close()
            client_connectionSocket.close()
            # print("From Proxy: Sockets for both client and server are closed")
            exit()


if __name__ == '__main__':
    # listenPort = "54333"
    # fakeIP = 'localhost'
    # serverIP = 'localhost'
    listenPort = sys.argv[1]
    fakeIP = sys.argv[2]
    serverIP = sys.argv[3]
    client2proxy2server(int(listenPort), fakeIP, serverIP)

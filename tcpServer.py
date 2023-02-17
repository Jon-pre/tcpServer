# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from socket import *
import _thread as thread


def broadcast(connection):
    connection.recv(1024)
    connection.send("Ny klient joinet server!".encode())


def handleClient(connection):
    while True:
        data = connection.recv(1024).decode()
        print("message recieved:", data)
        modified_msg = data.upper()
        connection.send(modified_msg.encode())
        if data == "exit":
            print("Connection is ended")
            break
        else:
            continue
    print("Server is shut down")
    thread.exit()
    connection.close()


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is running and listening")
while True:
    connectionsocket, addr = serverSocket.accept()
    print("Server connected by", addr)
    try:
        broadcast(connectionsocket, )
        thread.start_new_thread(handleClient, (connectionsocket,))
    except:
        print("Something went wrong")
serverSocket.close()

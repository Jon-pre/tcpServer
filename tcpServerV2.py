"""
Server side: it simultaneously handle multiple clients
and broadcast when a client new client joins or a client
sends a message.
"""
from socket import *
import _thread as thread
import time
import sys

# this is too keep all the newly joined connections!
all_client_connections = []


def now():
    """
    returns the time of day
    """
    return time.ctime(time.time())


def handleClient(connection, addr):
    """
    a client handler function
    """
    # this is where we broadcast everyone that a new client has joined

    ### Write your code here ###
    # append this this to the list for broadcast
    # create a message to inform all other clients
    # that a new client has just joined.
    all_client_connections.append(connection)
    connection.send('Welcome!'.encode())  # send data to the client
    broadcast(connection, str(addr) + " joined.")
    ### Your code ends here ###

    while True:
        message = connection.recv(2048).decode()
        print(now() + " " + str(addr) + "#  ", message)
        if (message == "exit" or not message):
            break
        ### Write your code here ###
        # broadcast this message to the others
        broadcast(connection, message)
    ### Your code ends here ###
    connection.close()
    all_client_connections.remove(connection)


def broadcast(connection, message):
    print("Broadcasting")
    ### Write your code here ###
    for other in all_client_connections:
        if other != connection:
            other.send(message.encode())  # send data to the client


### Your code ends here ###

def main():
    """
    creates a server socket, listens for new connections,
    and spawns a new thread whenever a new connection join
    """
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        # Use the bind function wisely!
        ### Write your code here ###
        serverSocket.bind(('127.0.0.1', serverPort))
    ### Your code ends here ###

    except:
        print("Bind failed. Error : ")
        sys.exit()
    serverSocket.listen(10)
    print('The server is ready to receive')
    while True:
        ### Write your code here ###
        connectionSocket, addr = serverSocket.accept()  # accept a connection
        ### You code ends here ###

        print('Server connected by ', addr)
        print('at ', now())
        thread.start_new_thread(handleClient, (connectionSocket, addr))
    # print(f"[ACTIV CONNECTIONS] {thread.acticeCount()-1}")
    serverSocket.close()


if __name__ == '__main__':
    main()




# Devon Long
# Python Programming: Web Server 
# Used the below resources for this assignment
# https://docs.python.org/3/library/socket.html
# https://pymotw.com/2/socket/tcp.html
# https://docs.python.org/3/howto/sockets.html#socket-howto


#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    hostIp = "127.0.0.1"
    print(sys.stderr, 'starting up on %s' % hostIp)
    serverSocket.bind((hostIp,port))
    serverSocket.listen()
    

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        
        try:
            message = connectionSocket.recv(4096).decode()
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            #Send one HTTP header line into socket
            connectionSocket.send(("HTTP/1.1 200 OK\r\n").encode())


            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            connectionSocket.send(("HTTP/1.1 404 Not Found\r\nContent-Type:text/html\r\n").encode())

            #Close client socket
            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)

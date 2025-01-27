import pickle
from socket import *

serverPort = 1787
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("127.0.0.1", serverPort))
serverSocket.listen(1)
print('Client-Server connection established')
while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        print("Client connection established")
        while True:
            data = connectionSocket.recv(1024)
            if data == b"EOF":
                print("\n......EOF from server......\n")
                break
            print("\nData Record",data)
        connectionSocket.send(("Data received").encode())
        connectionSocket.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Close the server socket when done
serverSocket.close()

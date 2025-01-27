from socket import *

serverPort = 1001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The cache is ready to receive')

while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        print(sentence)
        if not sentence:
            # Handle the case where no data is received.
            connectionSocket.close()
            continue
        capitalizedSentence = "Message from cache".encode()
        connectionSocket.send(capitalizedSentence)
        connectionSocket.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Close the server socket when done
serverSocket.close()

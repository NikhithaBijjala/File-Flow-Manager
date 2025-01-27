from socket import *
import sys
import pickle

def create_connection(serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    return clientSocket

def upload_file(file_path,serverconnection):
    file_name = file_path.split("/")[-1]
    print(file_name)
    # serverconnection.send(file_name.encode())
    try:
        serverconnection.send(file_name.encode())
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                print("data",data)
                if data == b'':
                    # serverconnection.send(b"EOF")
                    print("b''")
                    break
                serverconnection.send(data)
        serverconnection.send(b"EOF")
        response = serverconnection.recv(1024)
        if (response):
            print("File uploaded to server sucessfully")
        else:
            print("File uploadtion failed")
    except Exception as e:
        print(f"An error occurred: {e}")




def client_program():
    script_name = sys.argv[0]
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
    while True:
        command = input("Enter command\n ")
        option = command.split()
        if (option[0] == "put"):
            print("Uploading the file to server.....\n")
            # serverName = "localhost"
            # serverPort = 1347
            clientSocket = create_connection(serverName, serverPort)
            upload_file(option[1], clientSocket)

            # sentence = input("Input lowercase sentence:")
            # clientSocket.send(sentence.encode())
            # modifiedSentence = clientSocket.recv(1024)
            # print("From Server: ", modifiedSentence.decode())
            # clientSocket.close()
        elif (option == "get"):
            print("downloading.....\n")
            serverName = "localhost"
            serverPort = 1001
            clientSocket = create_connection(serverName, serverPort)
            sentence = input("Input to cache:")
            clientSocket.send(sentence.encode())
            modifiedSentence = clientSocket.recv(1024)
            print("From Cache: ", modifiedSentence.decode())
            clientSocket.close()
        elif (option == "quit"):
            print("Exiting program!")
            return



if __name__ == '__main__':
    client_program()
from socket import *
servername = "127.0.0.1"
serverport = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername,serverport))
sen = input("Input: ")
clientSocket.send(sen.encode())
m = clientSocket.recv(1024)
print("From server farenhiet:",m.decode())
clientSocket.close()

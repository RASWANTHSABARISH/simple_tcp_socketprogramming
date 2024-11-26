from socket import *
server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print("The server is ready to receive")
while True:
    # Accepting a connection
    connection_socket, addr = server_socket.accept()
    data = connection_socket.recv(1024).decode()
    celsius = float(data)
    fahrenheit = (celsius * 9 / 5) + 32
    connection_socket.send(str(fahrenheit).encode())
    connection_socket.close()
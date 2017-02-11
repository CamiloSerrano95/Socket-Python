import socket
import sys
serverName = 'localhost'
serverPort = 12000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')
client_socket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = client_socket.recvfrom(2048)
print (modifiedMessage)
client_socket.close()
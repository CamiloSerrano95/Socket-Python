import socket
import sys

serverName = 'localhost'
serverPort = 12000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


message1 = raw_input('Ingrese lado A del triangulo:')
message2 = raw_input('Ingrese lado B del triangulo:')
message3 = raw_input('Ingrese lado C del triangulo:')

triangulo = message1 + "_" + message2 + "_" + message3
 
client_socket.sendto(triangulo,(serverName, serverPort))
serverResponse, serverAddress = client_socket.recvfrom(2048)

print (serverResponse)

client_socket.close()
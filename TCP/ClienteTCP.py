import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 10008)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
	print ("Cual es su cedula")
	cedula = raw_input()
	sock.sendall(cedula)

	datos = sock.recv(100)

	datos = datos.split(",")
	print "Nombres: "+datos[0]+ "\n"
	print "Apellidos: "+datos[1]+ "\n"
	print "Cedula: "+datos[2]+ "\n"

	if datos[3]==1:
		print "jurado: Si" "\n"

	else:
		print "Jurado No" "\n"
	print "Lugar de votacion: "+datos[4]+ "\n"
	print "Mesa: "+datos[5]+ "\n"	

finally:
		print >>sys.stderr, 'closing socket'
		sock.close()

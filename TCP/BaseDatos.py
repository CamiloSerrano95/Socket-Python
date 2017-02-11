import MySQLdb
import sys

try: 
	db = MySQLdb.connect(
		host = '127.0.0.1',
		user = 'root',
		passwd = '1067943114',
		db = 'registraduria',
		)
except Exception as e: 
	sys.exit('No se puede conectar a la base de datos!!!')


"""def insertar():
	print ("Cual es su nombre")
	nombre = raw_input()

	print ("Cual es su apellido")
	apellido = raw_input()

	print ("Cual es su cedula")
	cedula = raw_input()

	print ("Es jurado?")
	jurado = raw_input()

	print ("Cual es su lugar de votacion")
	lugar_votacion = raw_input()

	print ("Numero de su mesa ")
	mesa = raw_input()

	cursor = db.cursor()
	stringQuery = "INSERT INTO usu (nombres, apellidos, cedula, jurado, lugar_votacion, mesa) VALUES ('"+nombre+"', '"+apellido+"', '"+cedula+"', '"+jurado+"', '"+lugar_votacion+"', '"+mesa+"')"
	cursor.execute(stringQuery)
	db.commit()"""

def consultar(cedula):
	
	cursor = db.cursor()
	stringQuery = "SELECT * FROM usu WHERE cedula='"+str(cedula)+"'"
	cursor.execute(stringQuery)
	datos = cursor.fetchone()
	
	string = str(datos[1])+","+str(datos[2])+","+str(datos[3])+","+str(datos[4])+","+str(datos[5])+","+str(datos[6])
	return string
	db.commit()

#consultar("123")
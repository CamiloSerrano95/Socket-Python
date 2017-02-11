def triangulo(data):
	message = data.split("_")

	if message[0] == message[1] == message[2]:
		response = "El triangulo es equilatero"
	elif message[0] == message[1] or message[1] == message[2] or message[0] == message[2]:
		response = "El triangulo es isoceles"
	else:
		response = "El triangulo es escaleno"

	return response
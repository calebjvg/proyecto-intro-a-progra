

ingre={"a":15, "b":16, "c":18}
nacionalidades= {1:"extranjero",2:"nacional"}
edades={1:"nino", 2:"adulto",3:"adulto mayor"}
def reserva():
	personas=[]
	cantidad = int(input("Cuantas personas serian:"))
	edad = []
	hora=[]
	for i in range(cantidad):
		

		print(f"Indique datos para persona {i+1}:")
		nacionalidad = int(input("1.Extranjero\n2.Nacional:\n"))
		edad = int(input("1.Nino\n2.Adulto\n3.Adulto Mayor:\n"))
		personas.append({"nacionalidad":nacionalidades[nacionalidad], "edad":edades[edad]})
	print(personas)
	
	# print("Horarios disponibles:")
	# print(dict, ("horas"))
	# horario=(input("ingrese horario disponible: ")) 
	return personas

# diccionario para

 

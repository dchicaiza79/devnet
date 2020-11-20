def contar_palabras(frase):
	palabras=[]
	cadena=frase.split()
	for i in cadena:
		palabras.append(i) 	
	print(palabras)
	print("La longitud es: "+str(len(frase)))

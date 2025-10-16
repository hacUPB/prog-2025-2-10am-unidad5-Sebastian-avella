archivo = open("./Archivos/Ejercicio1.txt", "r")
#archivo.readline()
#archivo.readline()
#archivo.read(17)
archivo.seek(10)
datos = archivo.readline()
print(datos)
archivo.close
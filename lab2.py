#Fernanda Ruiz y Rayen Lara
import hashlib
#Se recibe un txt y se almacena en una variable
with open("mensajedeentrada.txt") as archivo:
    texto=archivo.read()

#Funcion Hash (SHA-256) 
def calcular_sha_hash(texto):
    # Crea un objeto hash SHA
    sha = hashlib.sha256()
    
    # Actualiza el objeto hash con el texto convertido a bytes
    sha.update(texto.encode('utf-8'))
    
    # Devuelve el hash en formato hexadecimal
    return sha.hexdigest()


#Se aplica la funcion con la variable definida
resultado_sha = calcular_sha_hash(texto)

#Se almacena en un archivo de texto
with open("mensajeseguro.txt", "w") as archivo:
    # se almacena el resultado del hasheo en un nuevo archivo
    archivo.write(resultado_sha)

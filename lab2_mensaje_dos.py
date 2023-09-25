# Fernanda Ruiz y Rayén Lara
import requests
import json
import hashlib

#lee el archivo txt
with open("mensajedeentrada.txt") as archivo:
    texto=archivo.read()
  

#Se aplican metodos de cifrado al mensaje (Rot-15 y Vigenere)
def rot15(mensaje):
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    auxiliar = ""
    for i in mensaje:
        auxiliar = auxiliar + diccionario[(diccionario.find(i) + 15) % 26]
    return auxiliar

#abecedario
letras = "abcdefghijklmnopqrstuvwxyz"

A = dict(zip(letras, range(len(letras)))) #a las letras le asigna su numero o posición
B = dict(zip(range(len(letras)), letras)) #asigna números a las letras 

def vigenere(mensaje, contrasena):
    cifrado = ""
    i = 0
    for letra in mensaje:
        numero = (A[letra] + A[contrasena[i % len(contrasena)]]) % len(letras)
        cifrado += B[numero]
        i += 1
    return cifrado

#Se cifra el mensaje mediante el metodo anterior
def cifrar_mensaje(mensaje):
    mensaje_rot15 = rot15(mensaje)
    contraseña = "cvqnoteshrwnszhhksorbqcoas"
    mensaje_cifrado_vigenere = vigenere(mensaje_rot15, contraseña)
    return  mensaje_cifrado_vigenere

#Se almacena el cifrado para utilizarlo posteriormente
mensaje_cifrado = cifrar_mensaje(texto)

#Ahora se crean las funciones para descifrar
def desrot15(mensaje):
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    auxiliar = ""
    for i in mensaje:
        auxiliar = auxiliar + diccionario[(diccionario.find(i) - 15) % 26]
    mensaje = auxiliar
    return mensaje


letras = "abcdefghijklmnopqrstuvwxyz"
A = dict(zip(letras, range(len(letras))))
B = dict(zip(range(len(letras)), letras))


def desvig(cifra, contrasena):
    decifrado = ""
    i = 0
    for letra in cifra:
        numero = (A[letra] - A[contrasena[i % len(contrasena)]]) % len(letras)
        decifrado += B[numero]
        i += 1
    return decifrado

#Se descifra el mensaje con las funciones anteriores
def descifrar_mensaje(mensaje_cifrado):
    mensaje_rot15 = desrot15(mensaje_cifrado)
    nueva_contraseña = "cvqnoteshrwnszhhksorbqcoas"
    mensaje_descifrado_vigenere = desvig(mensaje_rot15, nueva_contraseña)
    return mensaje_descifrado_vigenere

#Se almacena el mensaje nuevamente
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)


#Funcion Hash (SHA-256) 
def calcular_sha_hash(texto):
    # Crea un objeto hash SHA
    sha = hashlib.sha256()
    
    # Actualiza el objeto hash con el texto convertido a bytes
    sha.update(texto.encode('utf-8'))
    
    # Devuelve el hash en formato hexadecimal
    return sha.hexdigest()

#Almacenamos el mensaje en un TXT
#Se aplica la funcion con la variable definida
resultado_sha2 = calcular_sha_hash(mensaje_descifrado)

#Se almacena en un archivo de texto
with open("mensajeseguro2.txt", "w") as archivo:
    # se almacena el resultado del hasheo en un nuevo archivo
    archivo.write(resultado_sha2)

print(mensaje_descifrado)

import socket
from cryptography.fernet import Fernet
import argparse

# Datos de conexion
IP = '127.0.0.1'
Puerto = 1333
Buffer = 2048

# Conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, Puerto))
s.listen(10)
(conn, addr) = s.accept()
print('Direccin de conexion:', addr)
while True:
    msj_cifrado = conn.recv(Buffer)
    conn.send(b"Enterado, BYE!")
    break
conn.close()

# Cifrado
file = open('clave.key', 'rb')
clave = file.read()
file.close()
cipher_suite = Fernet(clave)

mensajeBytes = cipher_suite.decrypt(msj_cifrado,None)
mensaje = mensajeBytes.decode()
print("Mensaje recibido:\n", mensaje)

import socket
from cryptography.fernet import Fernet
import argparse

# Argumentos
description = """Modo de uso:
    cliente.py -msj "Mensaje a enviar"""
parser = argparse.ArgumentParser(description='Port scanning',
                                epilog=description,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-msj", metavar='MSJ', dest="msj",
                    help="mensaje a enviar", required=True)
params = parser.parse_args()

# Objeto para cifrar
clave = Fernet.generate_key()
cipher_suite = Fernet(clave)

# Clave
file = open('clave.key', 'wb')
file.write(clave)
file.close()

# Convertir a Bytes
mensaje = params.msj
mensajeBytes = mensaje.encode()

# Ciframos
msj_cifrado = cipher_suite.encrypt(mensajeBytes)
print("Mensaje enviado:\n", mensaje)

# Datos de conexion
IP = '127.0.0.1'
Puerto = 1333
Buffer = 2048

# Conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, Puerto))
s.send(msj_cifrado)
respuesta = s.recv(Buffer).decode()
s.close()

print("Respuesta recibida:", respuesta)

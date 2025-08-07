from config import Config
import socket
import uuid
import hashlib


host = Config.Host
port = Config.Port


Fmq_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Fmq_server.bind(host,port)
Fmq_server.listen()


connection, address = Fmq_server.accept()


def fmq_buffer(connection):
    buffer = b''

    while True:
        chunk = connection.recv(1024)

        if not chunk:
            break

        buffer += chunk

        if b'/n':
            break

    return buffer.decode().strip()


token = fmq_buffer(connection).split()

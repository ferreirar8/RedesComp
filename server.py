#!/usr/bin/env python3

import socket
import sys

def create_server_socket(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', port))
        server_socket.listen(10)
        return server_socket
    except socket.error as msg:
        print(f"Error: {msg}")
        sys.exit()

def accept_client_connection(server_socket):
    try:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted incoming connection from client")
        print(f"Client IP, Port = {client_address}")
        return client_socket
    except socket.error as msg:
        print(f"Error: {msg}")
        sys.exit()

def receive_data(client_socket):
    try:
        buffer_size = 4096
        data = client_socket.recv(buffer_size)
        return data.decode('ascii')
    except socket.error as msg:
        print(f"Error: {msg}")
        sys.exit()

def main():
    port = 389
    server_socket = create_server_socket(port)
    print(f"Listening socket bound to port {port}")

    client_socket = accept_client_connection(server_socket)
    received_message = receive_data(client_socket)

    print(f"Received {len(received_message.encode('ascii'))} bytes from client")
    print(f"Message contents: {received_message}")

    try:
        client_socket.close()
        server_socket.close()
    except socket.error as msg:
        print(f"Error: {msg}")
        sys.exit()

    print("Sockets closed, now exiting")

if __name__ == "__main__":
    main()

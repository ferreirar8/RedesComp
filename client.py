import socket
import sys

IP = 'localhost'
PORT = 389
BUFFER_SIZE = 4096

def create_socket():
    try:
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print(f"Error: could not create socket. Description: {msg}")
        sys.exit()

def connect_socket(sock, ip, port):
    try:
        sock.connect((ip, port))
        print(f"Connecting to server at {ip} on port {port}")
        print("Connection established")
    except socket.error as msg:
        print(f"Error: Could not open connection. Description: {msg}")
        sys.exit()

def send_data(sock, data):
    try:
        sock.sendall(data)
    except socket.error as msg:
        print(f"Error: send() failed. Description: {msg}")
        sys.exit()

def receive_data(sock):
    try:
        return sock.recv(BUFFER_SIZE).decode('ascii')
    except socket.error as msg:
        print(f"Error: unable to recv(). Description: {msg}")
        sys.exit()

def main():
    s = create_socket()
    connect_socket(s, IP, PORT)

    print(" (1) Registo de candidato \n (2) Registo de votante \n (3) Lista de candidatos \n (4) Efectuar votação \n (5) Obter candidato mais votado")
    escolha = input()

    if escolha == '1':
        user = input("Utilizador: ")
        password = input("Password: ")
        info = f"{user} {password}"
        send_data(s, bytes(info, 'ascii'))

        if receive_data(s) == 'ok':
            ide = input('id: ')
            nome = input('nome: ')
            mand = f"{ide} {nome} C"
            send_data(s, bytes(mand, 'ascii'))

    elif escolha == '2':
        user = input("Utilizador: ")
        password = input("Password: ")
        info = f"{user} {password}"
        send_data(s, bytes(info, 'ascii'))

        if receive_data(s) == 'ok':
            ide = input('id: ')
            nome = input('nome: ')
            mand = f"{ide} {nome} V"
            send_data(s, bytes(mand, 'ascii'))

    elif escolha == '3':
        send_data(s, b"LIST_CANDIDATES")
        print("Lista de candidatos recebida:")
        print(receive_data(s))

    elif escolha == '4':
        print("Funcionalidade de votação não implementada.")

    elif escolha == '5':
        print("Obter candidato mais votado não implementado.")

    else:
        print("Escolha inválida. Por favor, tente novamente.")

    try:
        s.close()
        print("Sockets closed, now exiting")
    except socket.error as msg:
        print(f"Error: unable to close() socket. Description: {msg}")
        sys.exit()

if __name__ == "__main__":
    main()

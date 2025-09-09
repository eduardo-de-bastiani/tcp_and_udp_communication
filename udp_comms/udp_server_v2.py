from socket import socket, AF_INET, SOCK_DGRAM
import sys

# Verifica se o número da porta foi fornecido como argumento
if len(sys.argv) != 2:
    print("Uso: python3 UDPServer_v2.py <porta>")
    sys.exit(1)

# Pega a porta do argumento da linha de comando
server_port = int(sys.argv[1])

# Cria o socket do servidor
server_socket = socket(AF_INET, SOCK_DGRAM)

# Associa o socket à porta informada
server_socket.bind(('', server_port))

print(f"O servidor está pronto para receber na porta {server_port}")

while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper()
    server_socket.sendto(modified_message.encode(), client_address)
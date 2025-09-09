from socket import socket, AF_INET, SOCK_DGRAM

# Define o endereço do servidor e a porta
# 'localhost' se refere à própria máquina (IP 127.0.0.1)
server_name = 'localhost'
server_port = 12000

# Cria o socket do cliente
client_socket = socket(AF_INET, SOCK_DGRAM)

# 1. Cliente lê uma linha do teclado

while True:
    message = input("Digite uma frase em minúsculo: ")
    
    if message.lower() == 'sair':
        print("Encerrando o cliente.")
        break

    # 1. (continuação) Cliente envia os dados para o servidor
    # .encode() converte a string para bytes
    client_socket.sendto(message.encode(), (server_name, server_port))

    # 4. Cliente recebe a mensagem modificada do servidor
    modified_message, server_address = client_socket.recvfrom(2048)

    # 4. (continuação) Cliente exibe a linha na tela
    # .decode() converte os bytes recebidos de volta para string
    print("Resposta do servidor:", modified_message.decode())

# Fecha o socket
client_socket.close()
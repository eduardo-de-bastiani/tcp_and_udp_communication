from socket import socket, AF_INET, SOCK_STREAM

server_name = 'localhost'
server_port = 12000

while True:
    message = input("Digite uma frase em minúsculo: ")

    if message.lower() == 'sair':
        print("Encerrando o cliente.")
        break
        
    # Cria o socket do cliente (é recriado a cada iteração do loop)
    # AF_INET = IPv4, SOCK_STREAM = TCP
    client_socket = socket(AF_INET, SOCK_STREAM)
    
    # Estabelece a conexão com o servidor
    client_socket.connect((server_name, server_port))
    
    # 1. Envia a mensagem (não precisa anexar o endereço, pois a conexão já existe)
    client_socket.send(message.encode())
    
    # 4. Recebe a resposta do servidor
    modified_message = client_socket.recv(1024)
    
    # Exibe a resposta na tela
    print("Resposta do servidor:", modified_message.decode())
    
    # Fecha o socket da conexão
    client_socket.close()
from socket import socket, AF_INET, SOCK_DGRAM

# Define uma lista com os dois servidores (IP, porta)
servers = [
    ('localhost', 12000),
    ('localhost', 12001)
]

# Cria o socket do cliente
client_socket = socket(AF_INET, SOCK_DGRAM)

# Variável para controlar para qual servidor enviar a mensagem
turn = 0

print("Cliente iniciado. Digite 'sair' para encerrar.")
print(f"Enviando para Servidor 1 ({servers[0][0]}:{servers[0][1]}) e Servidor 2 ({servers[1][0]}:{servers[1][1]}) de forma alternada.")

while True:
    message = input("Digite uma frase em minúsculo: ")
    
    if message.lower() == 'sair':
        print("Encerrando o cliente.")
        break

    # Seleciona o servidor da vez
    # turn % 2 resultará em 0, 1, 0, 1, ...
    current_server = servers[turn % len(servers)]
    
    print(f"-> Enviando para {current_server[0]}:{current_server[1]}")

    # Cliente envia os dados para o servidor selecionado
    client_socket.sendto(message.encode(), current_server)

    # Cliente recebe a mensagem modificada do servidor
    modified_message, server_address = client_socket.recvfrom(2048)

    # Cliente exibe a resposta
    print(f"Resposta de {server_address[0]}:{server_address[1]} -> {modified_message.decode()}")
    print("-" * 20)

    # Incrementa o turno para o próximo servidor
    turn += 1

# Fecha o socket
client_socket.close()
from socket import socket, AF_INET, SOCK_STREAM

# Lista de servidores para conectar
servers = [
    ('localhost', 12000),
    ('localhost', 12001)
]

# Variável para alternar entre os servidores
turn = 0

print("Cliente TCP iniciado. Digite 'sair' para encerrar o cliente.")
print("Digite 'FIM' para encerrar TODOS os servidores.")

while True:
    message = input("Digite uma frase em minúsculo: ")

    # Se a mensagem for 'FIM', envia para TODOS os servidores
    if message.strip().upper() == 'FIM':
        print("Comando de encerramento detectado. Enviando 'FIM' para todos os servidores...")
        
        for server in servers:
            try:
                # Cria, conecta, envia e fecha para cada servidor da lista
                client_socket = socket(AF_INET, SOCK_STREAM)
                client_socket.connect(server)
                client_socket.send(message.encode())
                response = client_socket.recv(1024).decode()
                print(f"-> Resposta de {server[0]}:{server[1]}: {response}")
                client_socket.close()
            except ConnectionRefusedError:
                print(f"-> Servidor {server[0]}:{server[1]} já está offline.")
        
        print("Comando de encerramento enviado a todos os servidores. Encerrando o cliente.")
        break # Sai do loop principal e encerra o cliente

    if message.lower() == 'sair':
        print("Encerrando o cliente.")
        break

    # Lógica antiga para comunicação alternada (para mensagens que não são 'FIM')
    current_server = servers[turn % len(servers)]
    print(f"-> Conectando ao servidor {current_server[0]}:{current_server[1]}")

    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(current_server)
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Resposta de {current_server[1]}: {response}")
        client_socket.close()

    except ConnectionRefusedError:
        print(f"Erro: A conexão com o servidor {current_server[1]} foi recusada.")
        print("O servidor pode estar offline. Encerrando o cliente.")
        break

    turn += 1

print("Cliente finalizado.")
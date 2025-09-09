from socket import socket, AF_INET, SOCK_STREAM
import sys

# Verifica e obtém o número da porta dos argumentos
if len(sys.argv) != 2:
    print("Uso: python3 TCPServer_v2.py <porta>")
    sys.exit(1)

server_port = int(sys.argv[1])

# Cria o socket de boas-vindas
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)

print(f"O servidor TCP está pronto para receber na porta {server_port}")
print("Para encerrar, envie a mensagem 'FIM' de um cliente.")

# Flag para controlar o loop principal do servidor
running = True

while running:
    # Aceita uma nova conexão
    connection_socket, addr = server_socket.accept()
    print(f"Conexão recebida de {addr}")
    
    # Recebe a mensagem do cliente
    message = connection_socket.recv(1024).decode()
    
    # Verifica se a mensagem é o comando para finalizar
    if message.strip().upper() == 'FIM':
        print(f"Comando de encerramento recebido de {addr}.")
        print("Encerrando o servidor...")
        running = False # Altera a flag para sair do loop principal
        response = "Servidor encerrando. Adeus!"
        connection_socket.send(response.encode())
    else:
        # Se não for 'FIM', processa normalmente
        capitalized_message = message.upper()
        connection_socket.send(capitalized_message.encode())
        
    # Fecha o socket desta conexão específica
    connection_socket.close()
    print(f"Conexão com {addr} encerrada.")

# Fecha o socket principal do servidor
server_socket.close()
print("Servidor finalizado.")
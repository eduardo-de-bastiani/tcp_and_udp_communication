from socket import socket, AF_INET, SOCK_DGRAM

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))

print("O servidor está pronto para receber")
print("Para encerrar, envie a mensagem 'FIM' de um cliente.")

while True:
    # Aguarda o recebimento de uma mensagem
    message, client_address = server_socket.recvfrom(2048)
    
    # Decodifica a mensagem e remove espaços em branco extras
    decoded_message = message.decode().strip()
    
    # Verifica se a mensagem é o comando para finalizar
    if decoded_message.upper() == 'FIM':
        print(f"Comando de encerramento recebido de {client_address}.")
        print("Encerrando o servidor...")
        break  # Sai do loop infinito
        
    # Se não for 'FIM', continua a lógica normal
    modified_message = decoded_message.upper()
    server_socket.sendto(modified_message.encode(), client_address)

# Fecha o socket após sair do loop
server_socket.close()
print("Servidor finalizado.")
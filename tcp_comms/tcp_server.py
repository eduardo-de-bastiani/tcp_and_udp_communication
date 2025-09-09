from socket import socket, AF_INET, SOCK_STREAM

server_port = 12000

# Cria o socket de "boas-vindas" do servidor
# SOCK_STREAM indica que o protocolo é TCP
server_socket = socket(AF_INET, SOCK_STREAM)

# Associa o socket à porta
server_socket.bind(('', server_port))

# Coloca o socket em modo de escuta, aguardando por clientes.
# O argumento (1) é o número de conexões enfileiradas permitidas.
server_socket.listen(1)

print("O servidor TCP está pronto para receber")

# Loop infinito para aceitar conexões de clientes
while True:
    # Aceita uma conexão. A execução fica bloqueada aqui até um cliente se conectar.
    # Cria um novo socket (connection_socket) para a comunicação com este cliente específico.
    connection_socket, addr = server_socket.accept()
    print(f"Conexão recebida de {addr}")
    
    # 2. Servidor recebe os dados do cliente através do socket da conexão
    message = connection_socket.recv(1024).decode()
    
    # Converte para maiúsculas
    capitalized_message = message.upper()
    
    # 3. Servidor envia a mensagem modificada de volta para o cliente
    connection_socket.send(capitalized_message.encode())
    
    # Fecha o socket da conexão (mas o socket de boas-vindas continua aberto)
    connection_socket.close()
    print(f"Conexão com {addr} encerrada.")

import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode('utf-8'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12347))
server.listen(5)

clients = []
print("Сервер запущен. Ожидание подключений...")

while True:
    client_socket, addr = server.accept()
    print(f"Подключен новый клиент: {addr}")
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555)) # Localhost and a random port
server.listen()

print("Server is listening...")
client, address = server.accept()
print(f"Connected to {address}")

message = client.recv(1024).decode('utf-8')
print(f"Client says: {message}")
client.send("Message received!".encode('utf-8'))
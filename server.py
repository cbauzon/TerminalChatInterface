import socket
import threading
import colors

color = colors.colors()

# For testing purposes
HOST = "127.0.0.1"
PORT = 12345

# Gets host and port name of the computer running the server
# HOST = input("What is the IP address you want to host the server on?: ")
# PORT = int(input("What port # will the server be hosted on: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(conn, addr):
    conn.send("Welcome to the chat room!".encode())

    while True:
        try:
            message = conn.recv(1024)
            if message:
                print(f"Received: {message.decode()}")
                broadcast(message, conn)
            else:
                raise Exception("Client disconnected")
        except:
            clients.remove(conn)
            conn.close()
            break

print(f"{color.fg.cyan}Server is listening...{color.reset}")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    print(f"New client connected: {addr}")

    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()

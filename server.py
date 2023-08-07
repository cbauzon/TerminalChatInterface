import socket

# Gets host and port name of the computer running the server
HOST = socket.gethostname()
PORT = 12345

# Creates socket object, binds socket to addr, and opens socket for connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

# Initializes client list
clients = []

print(f"Chat server is listening on {HOST}:{PORT}")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

while True:
    conn, addr = s.accept()
    clients.append(conn)
    print(f"New client connected: {addr}")

    conn.send("Welcome to the chat room!".encode())

    while True:
        try:
            message = conn.recv(1024)
            if message:
                print(f"Recieved: {message.decode()}")
                broadcast(message, conn)
            else:
                raise Exception("Client disconnected")
        except:
            clients.remove(conn)
            conn.close()
            break

import socket
import threading

# For testing purposes
HOST = "127.0.0.1"
PORT = 12345

# HOST = input("What is the IP address that you want to connect to?: ")
# PORT = int(input("What is the port #: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(message.decode())
        except:
            print("Connection lost.")
            client.close()
            break

def send():
    while True:
        message = input("To server: ")
        client.send(message.encode())

receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

receive_thread.start()
send_thread.start()
import socket
import threading

HOST = ""
PORT = 12345

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
    while true:
        message = input()
        client.send(message.encode())

receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

receive_thread.start()
send_thread.start()
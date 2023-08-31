from socket import socket
from threads_py import start_new_thread

socket_client = socket()

socket_client.connect(("localhost", 8006))


@start_new_thread(daemon=True)
def server_data():
    while True:
        data = socket_client.recv(1024).decode("utf-8")
        if data == "exit":
            socket_client.close()
        print("server data:", data)


server_data()

while True:
    msg = input(">>>: ")
    socket_client.send(msg.encode("utf-8"))
    if msg == "exit":
        break


socket_client.close()

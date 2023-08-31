from socket import socket
from threads_py import start_new_thread


def get_ip():
    pass


default_port: int = 8006

socket_server = socket()

try:
    socket_server.bind(("localhost", default_port))
except PermissionError:
    print("port is occupied")
    exit(1)


socket_server.listen(5)

print("waiting for connection...")
connect, addr = socket_server.accept()
print("connect success")
connect.send(f"hello {addr},welcome to back!".encode("utf-8"))


@start_new_thread(daemon=True)
def client_data():
    while True:
        data = connect.recv(1024).decode("utf-8")
        if data == "exit":
            connect.close()
        print("client data:", data)


client_data()

while True:
    send_msg = input("send: ")
    if send_msg == "exit":
        break
    connect.send(send_msg.encode("utf-8"))

connect.close()
socket_server.close()

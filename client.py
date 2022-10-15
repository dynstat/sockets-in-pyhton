# import socket module
import socket
import threading

# function to handle the received data from the client continuously
def server_ne_kuch_bheja_kya(connected_server,nickname):
    while True:
        if connected_server:
            try:
                server_ka_bheja_hua_mssg = connected_server.recv(1024).decode()
                print("\33[2K",end="")
                # print("\r"+nickname+":"+server_ka_bheja_hua_mssg+"\nCLIENT:",end=" ")
                print(f"\rSERVER: {server_ka_bheja_hua_mssg}\n{nickname}:",end=" ")
            except:
                break
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host_to_be_connected = "127.0.0.1"
server_port_to_be_connected = 2005

c.connect((server_host_to_be_connected, server_port_to_be_connected))
nickname = input("Enter your chat-room name: ")
if nickname:
    c.send(f"{nickname}".encode())
else:
    c.send(f"CLIENT".encode())
    
# Thread to handling receiving mssgs from client independently
server_thread = threading.Thread(target=server_ne_kuch_bheja_kya, args=(c,nickname))
server_thread.start()

while True:
    mssg_to_send = input(f"\r{nickname}: ")
    if mssg_to_send != "exit!!":
        c.send(f"{mssg_to_send}".encode())
    else:
        c.send(f"{mssg_to_send}".encode())
        c.close()
        break

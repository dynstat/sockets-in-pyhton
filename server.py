# import socket module
import os
import socket
import sys
import threading

# function to handle the received data from the client continuously
def client_ne_kuch_bheja_kya(connected_client,nickname):
    global s
    while True:
        try:
            client_ka_bheja_hua_mssg = connected_client.recv(1024).decode()
            print("\33[2K",end="")
            # print("\r"+client_ka_bheja_hua_mssg+"\nSERVER:",end=" ")
            if client_ka_bheja_hua_mssg == "exit!!":
                print(f"{nickname} has closed the connection !!")
                connected_client.close()
                sys.exit(1)
                s.close()
                os._exit() 
                break
            print(f"\r{nickname}: {client_ka_bheja_hua_mssg}\nSERVER:",end=" ")
        except:
            break

# # creating a object of socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = "127.0.0.1"
server_port = 2005

s.bind((server_host, server_port)) 

s.listen()
client_nickname = None
print(f"SERVER is running at {server_host} on port {server_port}\n")
conn, addr = s.accept()
client_nickname = conn.recv(1024).decode()
if client_nickname:
    print(f"{client_nickname} has joined the server.")
else:
    client_nickname = "Someone"
    print(f"{client_nickname} has joined the server.")
        
    
    
conn.send(f"Hello {client_nickname}, Welcome to the server\n".encode())
conn.send("You can send your texts now...\n".encode())
# Thread to handling receiving mssgs from client independently
client_thread = threading.Thread(target=client_ne_kuch_bheja_kya, args=(conn,client_nickname))
client_thread.start()

while True:
    if conn:
        d = input("\rSERVER: ")
        try:
            if d != "exit!!" or not conn:
                conn.send(d.encode())
            else:
                print("Closing the Server because of exit!! command")
                conn.close()
                s.close()
                break
        except:
            print("Server closed because of no client")
            break
                
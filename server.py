# import socket module
import os
import socket
import sys
import threading
from time import sleep

# # creating a object of socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = "127.0.0.1"
server_port = 2005

s.bind((server_host, server_port))

s.listen()
client_nickname = None

print(f"SERVER is running at {server_host} on port {server_port}\n")


SHUTDOWN = 0
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
                # sys.exit(1)
                # s.close()
                # os._exit() 
                break
            print(f"\r{nickname}: {client_ka_bheja_hua_mssg}\nSERVER:: ",end="")
        except:
            break

def mssg_to_client(connected_client, nickname):
    global SHUTDOWN
    while True:
        

        try:
            if connected_client:
                mssg_to_send = input("\rSERVER: ")
                if mssg_to_send != "exit!!" and connected_client:
                    # print("in try")
                    if connected_client:
                        connected_client.send(mssg_to_send.encode())
                else:
                    print(f"SHUTTING THE SERVER DOWN (from mssg_to_client func)")
                    connected_client.close()
                    # s.close()
                    SHUTDOWN = 1
                    break
            else:
                print(f"{nickname} not found (deleting mssg_to_client for this client)")
                break    
        except Exception as e:
            SHUTDOWN = 1
            print(f"Server closed because of client fault -> {e}")
            connected_client.close()
            break

def main():
    while True and not SHUTDOWN:
        conn, addr = s.accept()
        if conn:
            handle_client_thread = threading.Thread(target=handle_client, args=(conn,))
            handle_client_thread.start()
        
def handle_client(conn):    
    THIS_CLIENT = 1
    client_nickname = conn.recv(1024).decode()
    if client_nickname:
        print("\33[2K",end="")
        print(f"\r{client_nickname} has joined the server.")
    else:
        client_nickname = "Someone"
        print("\33[2K",end="")
        print(f"\r{client_nickname} has joined the server.")
        
    
    conn.send(f"Hello {client_nickname}, Welcome to the server\n".encode())
    conn.send("You can send your texts now...\n".encode())
    # Thread to handling receiving mssgs from client independently
    client_thread_recv = threading.Thread(target=client_ne_kuch_bheja_kya, args=(conn,client_nickname))
    client_thread_recv.start()
    client_thread_send = threading.Thread(target=mssg_to_client, args=(conn,client_nickname))
    client_thread_send.start()

    # client_thread_recv.join()
    # client_thread_send.join()

if __name__ == "__main__":
    main_thread = threading.Thread(target=main, daemon=True)
    main_thread.start()
    
    count = 1
    while True:
        # print(f"\r    main number {count}, shutdown value = {SHUTDOWN}",end="")
        count +=1
        sleep(1)
        # main()
        if SHUTDOWN:
            print("Shutting down (from main)")
            break
            sys.exit(1)
            
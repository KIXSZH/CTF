import socket
import threading
import subprocess
import random

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port on which the server will listen
host = '127.0.0.1'
port = 12346

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(100)

print(f"Server is listening on {host}:{port}")


# Function to handle a single client connection
def handle_client(client_socket, addr):
    try:
        print(f"Connection from {addr} accepted.")

        # Send a welcome message to the client
        message = "Welcome to this ---FREE FLAG-SERVER--- \n"
        client_socket.send(message.encode('utf-8'))
        flag = "bYtE_BuSteRs{GET_THIS-FREE-FLAG}"
        while True:
            #
            data = client_socket.recv(1024).decode('utf-8')

            m1 = "(PRESS_ENTER TO GET THE FREE FLAG)\n\n"
            client_socket.send(m1.encode('utf-8'))
            msg = "\nPRESS cntl+c to exit\n"
            client_socket.send(msg.encode('utf-8'))
            msg = flag
            client_socket.send(msg.encode('utf-8'))



    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Remove the client socket from the list when the connection is closed

        client_socket.close()




while True:
    # Accept a client connection
    client_socket, addr = server_socket.accept()

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()

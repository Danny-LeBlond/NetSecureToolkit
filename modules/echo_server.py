# Filename: modules/echo_server.py

"""
Echo Server Module

Theprogram makes a server that waits for a client to connect.
When a client connects it gets a message and sends the same message back.

Function:
    run_server(host, port)

Parameters:
    host (str): The IP address to run the server on ( 127.0.0.1)
    port (int): The port number the server listens on

What it does:
    - Creates a server socket
    - Connects the server to a host and port
    - Waits for a client to connect
    - Accepts the connection
    - Gets data from the client
    - Prints the message and how many bytes were received
    - Sends the same message back to the client
    - Closes the connection and the server

"""


import socket


def run_server(host, port):
    try:
        server = socket.socket()
        server.settimeout(30)
        server.bind((host, port))
        server.listen(1)

        print("Server is waiting...")
        print("Host:", host)
        print("Port:", port)
        print("Timeout:", 30)

        conn, addr = server.accept()
        conn.settimeout(10)

        print("Connected by:", addr)
        print("Client IP:", addr[0])
        print("Client Port:", addr[1])

        data = conn.recv(1024)
        print("Bytes received:", len(data))
        print("Received:", data.decode())

        conn.sendall(data)
    

        conn.close()
        server.close()

    except socket.timeout:
        print("Error: connection timed out")
    except ConnectionError:
        print("Error: connection error happened")
    except OSError as e:
        print("Error:", e)
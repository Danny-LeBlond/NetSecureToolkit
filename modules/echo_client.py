# Filename: modules/echo_client.py

"""
Echo Client Module

The program connects to a server and sends a message.
The server sends the same message back so I know it worked.

Function:
    run_client(host, port, message)

Parameters:
    host (str): The server IP address ( 127.0.0.1)
    port (int): The port number to connect to
    message (str): The message to send to the server

What it does:
    - Creates a client socket
    - Connects to the server using a host and port
    - Shows connection details
    - Sends a message to the server
    - Receives the message back from the server
    - Prints the response and number of bytes received
    - Closes the connection

"""

import socket


def run_client(host, port, message):
    try:
        client = socket.socket()
        client.settimeout(10)

        client.connect((host, port))

        print("Connected to server ")
        print("Host:", host)
        print("Port:", port)
        print("Timeout:", 10)
        print("Local socket:", client.getsockname())
        print("Remote socket:", client.getpeername())

        print("Sending:", message)
        client.sendall(message.encode())

        data = client.recv(1024)
        print("Bytes received:", len(data))
        print("Got back:", data.decode())

        client.close()

    except socket.timeout:
        print("Error: connection timed out")
    except ConnectionRefusedError:
        print("Error: server is not running or refused the connection")
    except socket.gaierror:
        print("Error: bad host name")
    except OSError as e:
        print("Error:", e)
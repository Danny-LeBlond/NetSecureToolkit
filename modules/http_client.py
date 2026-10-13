# Filename: modules/http_client.py

"""
HTTP Client Module

The program connects to a website and sends a simple HTTP request.
It asks the server for the main page and then shows the response.

Function:
    run_http(host)

Parameters:
    host (str): The website to connect to (example.com)

What it does:
    - Connects to the website using port 80 (HTTP)
    - Sends a GET request to ask for the main page
    - Receives the response from the server
    - Splits the response into parts
    - Shows the status line, headers, and body
    - Prints the results to the screen

"""


import socket


def run_http(host):
    try:
        port = 80

        client = socket.socket()
        client.settimeout(30)

        print("Connecting to:", host, "on port", port)
        client.connect((host, port))

        request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"

        print("Sending HTTP request:")
        print(request)

        client.sendall(request.encode())

        response = client.recv(4096).decode()

        print("Raw response:")
        print(response)

        
        lines = response.split("\r\n")

        status_line = lines[0]
        print("Status Line:", status_line)

        print("\nHeaders:")
        i = 1
        while lines[i] != "":
            print(lines[i])
            i += 1

        print("\nBody:")
        body = "\n".join(lines[i+1:])
        print(body[:500])  # just prints first part so it's not huge

        client.close()

    except socket.timeout:
        print("Error: connection timed out")
    except socket.gaierror:
        print("Error: bad host name")
    except ConnectionRefusedError:
        print("Error: connection refused")
    except OSError as e:
        print("Error:", e)
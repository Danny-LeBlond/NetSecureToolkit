# Filename: modules/port_scanner.py

"""
Port Scanner Module:

The program scans a host to see which ports are open in a certain range.
It uses a TCP connect scan which means it tries to fully connect to each
port to see if it is open.

Function:
    run_scan(host, start_port, end_port)

Parameters:
    host (str): The host to scan 
    start_port (int): The starting port number
    end_port (int): The ending port number

What it does:
    - Turns the host name into an IP address
    - Loops through all the ports in the range
    - Tries to connect to each port
    - Finds which ports are open
    - Shows the service name
    - Prints the results to the screen
"""

import socket

def run_scan(host, start_port, end_port):
    print("Starting port scan...")
    print("Host:", host)
    print("Port range:", str(start_port) + "-" + str(end_port))
    print()

    try:
        target_ip = socket.gethostbyname(host)
        print("Resolved IP:", target_ip)
        print()
    except socket.gaierror:
        print("Error: bad host name")
        return

    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            scan_socket = socket.socket()
            scan_socket.settimeout(1)

            result = scan_socket.connect_ex((target_ip, port))

            if result == 0:
                try:
                    service_name = socket.getservbyport(port)
                except OSError:
                    service_name = "unknown"

                print("Port", port, "is open -", service_name)
                open_ports.append(port)

            scan_socket.close()

        except socket.timeout:
            print("Timeout on port", port)
        except OSError as error_message:
            print("Error on port", port, ":", error_message)

    print()
    print("Scan finished.")
    print("Total open ports found:", len(open_ports))
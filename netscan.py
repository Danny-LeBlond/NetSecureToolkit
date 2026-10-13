# Filename: netscan.py

"""
NetScan Main Program

This program is the main controller for the project. It lets the user run
different tools like the echo server, echo client, HTTP client, port scanner,
FTP client, SSH client, and the SQL injection demos from the command line.

Function:
    main()

What it does:
    - Reads command line arguments from the user
    - Decides which tool to run based on the input
    - Starts the echo server, echo client, HTTP client, port scanner, FTP client, or SSH client
    - Handles user input for port ranges when scanning
    - Allows downloading files from an FTP server
    - Connects to an SSH server, runs commands, and shows output
    - Starts the vulnerable SQL demo or the secure SQL demo
    - Shows example commands if nothing is entered

Notes:
    - will add to this as I make more mods
"""



import argparse
import subprocess
import sys
from modules.echo_server import run_server
from modules.echo_client import run_client
from modules.http_client import run_http
from modules.port_scanner import run_scan
from modules.ftp_client import run_ftp
from modules.ssh_client import run_ssh

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--server", action="store_true")
    parser.add_argument("--client")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--http")
    parser.add_argument("--scan")
    parser.add_argument("--ports")
    parser.add_argument("--ftp")
    parser.add_argument("--download")
    parser.add_argument("--ssh")
    parser.add_argument("--user")
    parser.add_argument("--sqlvuln", action="store_true")
    parser.add_argument("--sqlsecure", action="store_true")
    parser.add_argument("--password")
    parser.add_argument("--command")
    args = parser.parse_args()
 
    if args.server:
        print("Starting Echo Server...")
        run_server(args.host, args.port)

    elif args.client:
        print("Starting Echo Client...")
        run_client(args.host, args.port, args.client)

    elif args.http:
        print("Starting HTTP Client...")

        url = args.http.strip()

        if url.startswith("http://"):
            url = url.replace("http://", "")
        elif url.startswith("https://"):
            url = url.replace("https://", "")

        if url.endswith("/"):
            url = url[:-1]

        run_http(url)
    elif args.scan:
        print("Starting Port Scanner...")
      
        if not args.ports:
            args.ports = input("Enter port range (example 1-100): ")

     
        while True:
            port_parts = args.ports.split("-")

            if len(port_parts) != 2:
                print("Error: ports must be in format start-end (example: 1-100)")
                args.ports = input("Enter ports: ")
                continue

            if not port_parts[0].isdigit() or not port_parts[1].isdigit():
                print("Error: ports must be numbers (example: 1-100)")
                args.ports = input("Enter ports: ")
                continue

            start_port = int(port_parts[0])
            end_port = int(port_parts[1])
            break

        run_scan(args.scan, start_port, end_port)

    elif args.ftp:
        print("Starting FTP Client...")
        run_ftp(args.ftp, args.download)
    
    elif args.ssh:
        print("Starting SSH Client...")

        if not args.user or not args.password or not args.command:
            print("Error: need --user, --password, and --command")
            return

        run_ssh(args.ssh, args.user, args.password, args.command)

    elif args.sqlvuln:
        print("Starting Vulnerable SQL Demo...")
        subprocess.run([sys.executable, "modules/sql_demo.py"])

    elif args.sqlsecure:
        print("Starting Secure SQL Demo...")
        subprocess.run([sys.executable, "modules/sql_demo_secure.py"]) 

    else:
        print("Examples:")
        print("python netscan.py --server")
        print('python netscan.py --client "hello"')
        print("python netscan.py --http example.com")
        print("python netscan.py --http https://example.com")
        print("python netscan.py --scan 127.0.0.1 --ports 1-100")
        print("python netscan.py --scan example.com --ports 1-1000")
        print("python netscan.py --ftp example.com")
        print("python netscan.py --ftp example.com --download file.txt")
        print("python netscan.py --ftp ftp.cs.brown.edu")
        print("python netscan.py --ftp ftp.cs.brown.edu --download README")
        print('python netscan.py --ssh 127.0.0.1 --user your_username --password your_password --command "whoami"')
        print('python netscan.py --ssh 127.0.0.1 --user your_username --password your_password --command "dir"')
        print('python netscan.py --ssh test.rebex.net --user demo --password password --command "ls"')
        print("python netscan.py --sqlvuln")
        print("python netscan.py --sqlsecure")


if __name__ == "__main__":
    main()
## Author
Danny LeBlond

## Course
Security Libraries in Programming Languages

## Date
April 12th, 2026

## Table of Contents:
    Echo Client lines: 32-78
    Echo_server lines: 83-146
    http_client lines: 151-231
    netscan lines:     235-340
    
    How to Run:        350-444

    Phase 1:           30-340
    Phase 2:           456-541
    Phase 3:           547-749
    Phase 4:           760-764
    Phase 5:           775-1040
    Phase 6:           1046-1060






# Phase 1: Sockets & Custom HTTP Client

Echo Client (echo_client.py)

The echo client: This program connects to a TCP server running on the same computer (localhost / 127.0.0.1) and sends a message. The server then sends the same message back so we know the connection is working.

    Explanation:

            import socket: Imports the socket library,  lets the program send and receive data.

            def run_client(host, port, message): Creates a function that takes in a host (IP address or domain name), a port number, and a message to send.

            client = socket.socket() Creates a new socket. Tool that lets two programs talk to each other. In this case, it connects to the same computer.

            client.settimeout(10) Sets a 10 second limit so the program does not wait forever if something goes wrong.

            client.connect((host, port)) Connects the client to the server using the host and port.

            print(...) Lines that show details about the connection so we can see what is happening:

                    Connected to server: Confirms successfully connected to the server.

                    Host: Shows which host you connected to ( usually 127.0.0.1,  your own computer).

                    Port: Port number being used (5000). Tells you which "door" on the computer the program is using.

                    Timeout 10: How long the client will wait (in seconds) before giving up.

                    Local socket:, client.getsockname(): Your side of the connection (your IP and port your computer picked).

                    Remote socket:, client.getpeername(): Servers side of the connection (the IP and port you connected to).

            client.sendall(message.encode()) Sends the message to the server. The message is changed into bytes using encode() .

            data = client.recv(1024) This receives data from the server. number 1024  (it will read up to 1024 bytes).

            data.decode() changes the received bytes back into normal text.

            client.close() closes the connection.

    Error Handling

            except socket.timeout: The program waited too long (more than 10 seconds) and the server did not respond. It stops and shows an error.

            except ConnectionRefusedError: The client tried to connect, but the server was not running or not listening on that port. 

            except socket.gaierror: The host name was wrong.

            except OSError as e: Catches any other errors.




Echo Server (echo_server.py)

The echo server: This program waits for a client to connect on the same computer (localhost / 127.0.0.1). When a client connects, it receives a message and sends the same message back.

        Explanation:

                import socket: imports the socket library so the program can use networking.

                def run_server(host, port):Creates a function that takes in a host (IP address) and a port number.

                server = socket.socket() Creates a socket for the server. It will be used to wait for connections.

                server.settimeout(30) Sets a 30 second limit so the server doesn't wait forever for a client to connect.

                server.bind((host, port)) Attaches the server to the host and port. Tells the program where to listen for connections.

                server.listen(1) Tells the server to start listening for incoming connections. The number 1 means it will handle one connection.

                print(...) Lines show that the server is running and waiting for a connection:

                        Server is waiting:  the server is ready.

                        Host:  where the server is running (usually 127.0.0.1).

                        Port:  the port being used (like 5000).

                        Timeout: how long the server will wait.

                conn, addr = server.accept() Waits for a client to connect. When a client connects, it creates a new connection (conn) and stores the clients address (addr).

                conn.settimeout(10) Sets a timeout for the connected client .

                print(...) Lines show information about the connected client:

                        Connected by:  the clients IP and port.

                        Client IP:  the IP address of the client.

                        Client Port:  the port the client used.

                data = conn.recv(1024) Receives data from the client.

                data.decode() Converts the received bytes into normal text.

                print(...) Shows what the server received:

                        Bytes received: how many bytes came in from the client.

                        Received:actual message after it is decoded into text.

                conn.sendall(data) Sends the same data back to the client.

                conn.close() Closes the connection with the client.

                server.close() Shuts down the server.

       
        Error Handling:

                except socket.timeout: The server waited too long and no client connected. It stops and shows an error.

                except ConnectionError: Something went wrong with the connection between the client and server.

                except OSError as e: Catches any other errors and prints them.




HTTP Client (http_client.py)

The HTTP client: This program connects to a real web server on the internet (like example.com) using port 80. It sends a manual HTTP request and then reads and displays the response.

        Explanation:

                import socket: imports the socket library so the program can send and receive data.

                def run_http(host): Creates a function that takes in a host (domain name like example.com).

                port = 80 Sets the port to 80.

                client = socket.socket() Creates a socket to connect to the web server.

                client.settimeout(30) Sets a 30 second limit so the program does not wait forever.

                print(...) Shows what the program is doing:

                        Connecting to: shows the website and port being used.

                client.connect((host, port)) Connects to the web server.

                request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n" creates a manual HTTP request.

                        GET / HTTP/1.1 asks for the main page.

                        Host: tells the server which website.

                        \r\n\r\n the request is finished.

                print(...) Shows the request being sent.

                client.sendall(request.encode()) Sends the HTTP request to the server.

                response = client.recv(4096).decode() Receives the response from the server and converts it to text.

                print(...) Shows the raw response from the server.

                lines = response.split("\r\n") Splits the response into lines so it can be read.

                status_line = lines[0] Gets the first line of the response .

                print("Status Line:", status_line) Shows the status line.

                print("Headers:") and loop:
                Prints all the headers.

                print("Body:") Shows the actual webpage content.

                body = "\n".join(lines[i+1:])
                Combines the remaining lines into the body.

                print(body[:500]) Prints only the first part of the body so it is not huge.

                client.close() Closes the connection.



        Error Handling:

                except socket.timeout: The server took too long to respond.

                except socket.gaierror: The host name was wrong or could not be found.

                except ConnectionRefusedError: The connection was rejected.

                except OSError as e: Catches any other errors and prints them.


        HTTP Request Format:
                The HTTP request sent by this program looks like this:
                GET / HTTP/1.1
                Host: example.com


                GET: This is the request method. It means we are asking the server for data.
                /: This is the path. Asking for the main page of the website.
                HTTP/1.1: version of the HTTP protocol being used.
                Host: example.com:  which website we are trying to reach. 
                \r\n: special characters that mean new line. HTTP uses them to separate parts of the request.
                \r\n\r\n:  request is finished and ready to be sent to the server.



Netscan (netscan.py)

The netscan file: This program is the main controller. It lets you choose what part of the project to run (server, client, HTTP client, port scanner, FTP client, or SSH client).


    Explanation:

            import argparse: Imports a library that lets the program read commands from the terminal.

            from modules...: Imports the functions from the other files so this file can use them.

            def main(): Creates the main function that runs the program.

                parser = argparse.ArgumentParser() Sets up the argument so it can read user input.

                parser.add_argument("--server", action="store_true") If you type --server it will run the echo server.

                parser.add_argument("--client") If you type --client it will run the echo client and send a message.

                parser.add_argument("--host", default="127.0.0.1") Sets the default host (your own computer).

                parser.add_argument("--port", type=int, default=5000) Sets the default port (5000).

                parser.add_argument("--http") If you type --http it will run the HTTP client and connect to a website.

                parser.add_argument("--scan") If you type --scan it will run the port scanner.

                parser.add_argument("--ports") Lets the user give a port range for the scanner.

                parser.add_argument("--ftp") If you type --ftp it will run the FTP client.

                parser.add_argument("--download") Lets the user give a file name to download from the FTP server.

                parser.add_argument("--ssh") If you type --ssh it will run the SSH client.

                parser.add_argument("--user") Lets the user give a username for SSH login.

                parser.add_argument("--password") Lets the user give a password for SSH login.

                parser.add_argument("--command") Lets the user give a command to run on the SSH server.

                args = parser.parse_args() Reads the command line input and stores it.

                if/elif statements: Checks what option you picked and runs the correct part of the program:

                        print("Starting Echo Server..."): Shows that the echo server is starting.

                        run_server(args.host, args.port): Runs the echo server using the host and port.

                        print("Starting Echo Client..."): Shows that the echo client is starting.

                        run_client(args.host, args.port, args.client): Runs the echo client and sends your message.

                        print("Starting HTTP Client..."): Shows that the HTTP client is starting.

                        run_http(args.http): Runs the HTTP client and connects to a website.

                        print("Starting Port Scanner..."): Shows that the port scanner is starting.

                        if not args.ports: Checks if the user gave a port range. If not, it asks for one.

                        while True: Keeps asking until the port range is typed in correctly.

                                if len(port_parts) != 2: Checks if the port range is in the right format.

                                if not port_parts[0].isdigit() or not port_parts[1].isdigit(): Checks if both ports are numbers.

                                run_scan(args.scan, start_port, end_port): Runs the port scanner.

                                print("Starting FTP Client..."): Shows that the FTP client is starting.

                                run_ftp(args.ftp, args.download): Runs the FTP client and can download a file if one is given.

                                print("Starting SSH Client..."): Shows that the SSH client is starting.

                        if not args.user or not args.password or not args.command: Checks if the user gave all needed SSH information.

                                run_ssh(args.ssh, args.user, args.password, args.command): Runs the SSH client.

                else: If nothing is entered it prints examples so the user knows how to run the program.

                        print("Examples:"): Label for the example commands.

                        print("python netscan.py --server"): to start the echo server.

                        print('python netscan.py --client "hello"'): to run the echo client.

                        print("python netscan.py --http example.com"): to run the HTTP client.

                        print("python netscan.py --scan 127.0.0.1 --ports 1-100"): to run the port scanner.

                        print("python netscan.py --scan example.com --ports 1-1000"): to run the port scanner with a bigger range.

                        print("python netscan.py --ftp example.com"): to run the FTP client.

                        print("python netscan.py --ftp example.com --download file.txt"): to run the FTP client and try to download a file.

                        print("python netscan.py --ftp ftp.cs.brown.edu"): to run the FTP client on the test server.

                        print("python netscan.py --ftp ftp.cs.brown.edu --download README"): to run the FTP client and download a file.

                        print('python netscan.py --ssh 127.0.0.1 --user your_username --password your_password --command "whoami"'): to run the SSH client on your own computer.

                        print('python netscan.py --ssh 127.0.0.1 --user your_username --password your_password --command "dir"'): to run another SSH command on your own computer.

                        print('python netscan.py --ssh test.rebex.net --user demo --password password --command "ls"'): to run the SSH client on the test server.









How to Run

All commands are run in the terminal (Command Prompt or VS Code terminal).
           

           Step 1: Go to the Project Folder
                Go to the folder where netscan.py is saved:
                                                                cd "path to your NetSecureToolkit folder"

           Step 2: Run Features

                Run one command at a time depending on what you want to test. If you run netscan.py without any options, it will show you a list of example commands you can use.

                                Echo Server / Client
                                                Start the Echo Server first:
                                                        python netscan.py --server

                                                                Then open a second terminal and run the Echo Client:
                                                                                                python netscan.py --client "hello"






                                HTTP Client
                                        Connect to a website:
                                                        python netscan.py --http example.com

                                                You can also use https:   python netscan.py --http https://example.com






                                Port Scanner

                                        Scan ports on a target:
                                                        python netscan.py --scan 127.0.0.1 --ports 1-100

                                                        If you dont include --ports, the program will ask you to enter a range.






                                FTP Client

                                        Connect to an FTP server:
                                                                python netscan.py --ftp ftp.cs.brown.edu

                                        Download a file:
                                                        python netscan.py --ftp ftp.cs.brown.edu --download README





                                SSH Client

                                        Connect to an SSH server and run a command:
                                                                python netscan.py --ssh test.rebex.net --user demo --password password --command "ls"




                                SQL Injection Demo (Vulnerable)
                                        Start the vulnerable SQL demo:
                                                        python netscan.py --sqlvuln

                                                        Then open a browser and go to (The SQL demo run a web server, so you need to open a browser to use):
                                          
                                          
                                                                                 http://127.0.0.1:5000/





                                SQL Injection Demo (Secure)
                                                Start the secure SQL demo (The SQL demo run a web server, so you need to open a browser to use):
                                                                python netscan.py --sqlsecure

                                                                                Then open a browser and go to:
                                                                                                http://127.0.0.1:5000/



Important Notes

Some features (like Echo Server and Client) need two terminals.

Always start the server before running the client.











Phase 2:

## Table of Contents:

port_scanner lines:    464-520
Security discussion:   524- 541


Port Scanner (port_scanner.py)

        The port scanner: This program checks a host  to see which ports are open. It tries to connect to each port in a range and tells you which ones are open and what service might be running on them.


                Explanation:

                        import socket: Imports the socket library so the program can do network connections.

                        def run_scan(host, start_port, end_port): Creates a function that takes in a host, a starting port, and an ending port.

                        print(...): Shows what the program is doing:

                                Starting port scan: the scan has started.

                                Host: The host you are scanning.

                                Port range: Shows the range of ports being scanned.

                        target_ip = socket.gethostbyname(host) Converts the host name into an IP address.

                        print("Resolved IP:"):  the actual IP address of the host.

                        open_ports = [] Creates a list to store all the open ports found.

                        for port in range(start_port, end_port + 1): Loops through every port in the range.

                        scan_socket = socket.socket() Creates a new socket for each port.

                        scan_socket.settimeout(1) Sets a short timeout so it does not wait too long on each port.

                        result = scan_socket.connect_ex((target_ip, port)) Tries to connect to the port.

                                If result == 0: The port is open.

                        socket.getservbyport(port) Tries to find the service name for that port.

                                If it fails it sets the service name to "unknown".

                        print("Port ... is open"): Shows which ports are open and their service names.

                        open_ports.append(port) Saves the open port into the list.

                        scan_socket.close() Closes the socket after checking the port.

                        print("Scan finished"): Shows the scan is done.

                        print("Total open ports found"): Shows how many open ports were found.


                Error Handling:

                        except socket.gaierror: The host name was wrong and could not be converted to an IP address.

                        except socket.timeout: The connection to a port took too long and timed out.

                        except OSError as error_message: Catches other errors and prints them.

        

Security discussion:

                                        Difference between TCP connect scan and SYN scan:
                                                A TCP connect scan is what this program uses. It tries to fully connect to each port like a normal connection. If it connects, the port is open. This is simpler but it is slower .

                                                A SYN scan is different. It only sends the first step of the connection and checks the response without fully connecting. This makes it faster and harder to detect, but it usually needs more advanced tools.



                                        Legal implications:

                                                Port scanning without permission can be illegal. Even if it seems harmless, it can look like you are trying to find weak spots in someone else's stuff, and if you don't work for them, the company will think worst-case scenario and think you're trying to hack them or do something bad.



                                        IDS detection:

                                                 An IDS (Intrusion Detection System) is used to watch for suspicious activity on a network. TCP connect scans are easier to detect because they fully connect, which makes logs and alerts. SYN scans are harder to detect because they do not finish the full connection but advanced IDS systems can still notice scanning actions. Systems detect scans by looking for patterns like one computer trying to connect to many different ports really fast. If a computer is trying to connect really fast to a lot of different ports that looks weird and the system would flag it and log it. 





Phase 3:

## Table of Contents:
        ftp_client lines:       556-649
        ssh_client lines:       658-732
        Security discussion:    740-749



        ## FTP Client (ftp_client.py) 

The FTP client: This program connects to an FTP server, logs in using anonymous login, shows the files on the server, and can download a file if you give one.


        Explanation:

                from ftplib import FTP
                This imports the FTP library so the program can connect to FTP servers.

                def run_ftp(host, file_name=None):
                This creates a function that takes in a host (FTP server) and an optional file name to download.

                        print("Connecting to FTP server...")
                        print("Host:", host)
                        This shows what server the program is connecting to.

                        ftp = FTP(host)
                        This connects to the FTP server.

                        ftp.set_pasv(True)
                        This turns on passive mode so it works better with networks and firewalls.

                        print("Trying anonymous login...")
                        This shows the program is trying to log in.

                        ftp.login()
                        This logs into the FTP server using anonymous login (no username or password needed).

                        print("Connected!")
                        This shows the connection worked.

                        print()
                        This just adds a blank line to make the output easier to read.

                        print("Changing to pub directory...")
                        This shows the program is switching to the public folder.

                        ftp.cwd("pub")
                        This changes the folder to "pub", where public files are usually stored.

                        print("Files on server:")
                        This shows the program is about to list the files.

                        files = ftp.nlst()
                        This gets a list of all files in the current folder.

                        for file in files:
                                print(file)
                        This loops through each file and prints its name.

                        if file_name:
                        This checks if the user gave a file name to download.

                                print()
                                print("Trying to download:", file_name)
                                This shows which file is being downloaded.

                                with open(file_name, "wb") as f:
                                This opens a file on your computer so it can save the download.

                                ftp.retrbinary("RETR " + file_name, f.write)
                                This downloads the file from the FTP server and saves it.

                                print("Download complete!")
                                This shows the download finished.

                        ftp.quit()
                        This closes the FTP connection.


        Error Handling:

                except Exception as e:
                This catches any errors that happen in the program.

                        Examples of errors:
                        server not reachable
                        login failed
                        file not found
                        permission denied

                        print("Error:", e)
                        This prints the error so you know what went wrong.



Discussion:                        
Cleartext credential transmission:
FTP sends usernames and passwords in plain text so they are not protected. Anyone on the network can see the login info. Even with anonymous login the credentials are still sent without encryption.


Why FTP is insecure
  FTP is insecure because it does not encrypt data. This means usernames, passwords and files can be seen by others on the network. Because of this it is easy for hackers to steal info.








## SSH Client (ssh_client.py)

The SSH client: This program connects to an SSH server, tries to log in, runs a command, and shows the output.


    Explanation:

            import paramiko
            This imports the paramiko library so the program can connect to SSH servers.

            def run_ssh(host, username, password, command):
            This creates a function that takes in a host (SSH server), username, password, and a command to run.

                print("Connecting to SSH server...")
                print("Host:", host)
                This shows what server the program is connecting to.

                client = paramiko.SSHClient()
                This creates a new SSH client.

                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                This lets the program connect without asking about the server key.

                print("Trying to log in...")
                This shows the program is trying to log in.

                client.connect(host, username=username, password=password, timeout=10)
                This connects to the SSH server using the username and password.

                print("Connected")
                This shows the connection worked.

                print()
                This adds a blank line to make the output easier to read.

                print("Running command:", command)
                This shows what command is being run.

                stdin, stdout, stderr = client.exec_command(command)
                This runs the command on the server.

                output = stdout.read().decode()
                This gets the output from the command and turns it into text.

                errors = stderr.read().decode()
                This gets any error messages from the command.

                print("Output:")
                print(output)
                This prints the result of the command.

                if errors:
                This checks if there were any errors.

                    print("Errors:")
                    print(errors)
            This prints the error messages if there are any.

            client.close()
            This closes the SSH connection.


    Error Handling:

            except paramiko.AuthenticationException:
            This happens when the username or password is wrong.

            print("Error: bad username or password")
            This shows a login error.

            except Exception as e:
            This catches any other errors.

                print("Error:", e)
                This prints the error so you know what went wrong.







Discussion:

Key-based vs password authentication:
        Password authentication uses a username and password to log in which can be guessed or stolen. Key based authentication uses a private key which uses a long random key that cant realistically be guessed so it is more secure.

Brute force risks:
        Brute force attacks try many password guesses until one works. If passwords are weak, they can be cracked easily. Strong passwords are harder to guess and key based login uses a very large key space so it is not realistic to brute force.

Security analysis comparison: FTP vs SSH:
        FTP is not secure because it does not encrypt data. SSH is secure because it encrypts everything, including login info and commands. This makes SSH much safer than FTP.










Phase 4:

        ALL OF PHASE FOUR IS IN THE DOCS FOLDER ---> Phase 4 folder (after fixes.txt, before fixes.txt, Phase 4 fixes.docx and Phase 4 vulnerabilities.docx)

        This phase focuses on analyzing insecure Python code, exploiting the vulnerabilities, and then fixing them. The before and after files show the code changes, and the documents explain what the problems were and how they were fixed.










Phase 5:
                        Table of Contents:

                        sql_demo lines:          (vulnerable)   785-908
                        sql_demo_secure lines:   (secure)       915-1028
                        Reflection lines:                       1032-1042




SQL Demo (sql_demo.py)

        The SQL demo: This program shows how SQL injection works by using a login system that is not safe on purpose.


                Explanation:

                        from flask import Flask, request
                        Imports Flask so the program can run a web app and take user input from a form.

                        import sqlite3
                        Imports SQLite so the program can create and use a database.

                        app = Flask(__name__)
                        Creates the Flask app so the routes can run and the web server can start.

                        def init_db():
                        Creates a function to set up the database.

                                conn = sqlite3.connect("users.db")
                                Connects to a database file called users.db.

                                cursor = conn.cursor()
                                Creates a cursor which is used to send SQL commands to the database and get results back.

                                cursor.execute("""
                                CREATE TABLE IF NOT EXISTS users ...
                                """)
                                Creates a users table if it does not already exist.

                                cursor.execute("DELETE FROM users")
                                Clears old data so users do not get added multiple times.

                                cursor.execute("INSERT INTO users ...")
                                Adds test users like admin and user.

                                conn.commit()
                                Saves the changes.

                                conn.close()
                                Closes the database.

                        @app.route("/")
                        Connects the / URL to this function. When you open the site in your browser this is the first page you see.

                        def home():
                        Shows the login form in the browser so the user can type a username and password to try logging in.

                        @app.route("/login", methods=["POST"])
                        Connects the /login URL to this function. When the user clicks the login button the form data gets sent here to be checked.

                        def login():
                        Handles the login process.

                                username = request.form["username"]
                                Gets the username that the user typed into the login form.

                                password = request.form["password"]
                                Gets the password that the user typed into the login form.

                                conn = sqlite3.connect("users.db")
                                Opens a connection to the database so it can check the login info.

                                cursor = conn.cursor()
                                Sets up a way for the program to talk to the database so it can run the login check and see if the username and password match.

                                query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
                                Is the vulnerable part. It takes whatever the user typed and sticks it right into the SQL command as if it was part of the code. That means a user can type special characters and change what the query does instead of just checking their username and password.

                                print("Running query:", query)
                                Shows the query being run.

                                cursor.execute(query)
                                Runs the SQL query.

                                result = cursor.fetchone()
                                Gets one matching row if login works.

                                conn.close()
                                Closes the database.

                                if result:
                                        return "Login successful"
                                If a row is found login works.

                                else:
                                        return "Login failed"
                                If not login fails.


                        @app.route("/dump")
                        Connects the /dump URL to this function. When you go to this page in the browser it shows all users in the database.

                        def dump():
                        Handles showing the data from the database.

                                conn = sqlite3.connect("users.db")
                                Opens the database so it can read the data.

                                cursor = conn.cursor()
                                Sets up a way for the program to talk to the database.

                                cursor.execute("SELECT * FROM users")
                                Asks the database for all rows in the users table.

                                rows = cursor.fetchall()
                                Gets all the data returned from the database.

                                conn.close()
                                Closes the database.

                                return str(rows)
                                Sends the data back to the browser so you can see all users.Why this is unsafe:

                        - The program trusts user input
                        - The user can change the SQL query
                        - This allows SQL injection


                        Example attack:

                                ' OR '1'='1

                        This can trick the login and let anyone in.






SQL Demo Secure (sql_demo_secure.py)
        The secure version: This program fixes the problem by handling user input safely.



                Explanation:

                        from flask import Flask, request
                        Imports Flask so the program can run a web app.

                        import sqlite3
                        Imports SQLite for the database.

                        app = Flask(__name__)
                        Creates the Flask app so the routes can run and the web server can start.

                        def init_db():
                        Creates the database setup function.

                                conn = sqlite3.connect("users.db")
                                Connects to the database.

                                cursor = conn.cursor()
                                Sets up a way for the program to talk to the database.

                                cursor.execute("CREATE TABLE IF NOT EXISTS users ...")
                                Creates the users table.

                                cursor.execute("DELETE FROM users")
                                Clears old data.

                                cursor.execute("INSERT INTO users ...")
                                Adds test users.

                                conn.commit()
                                Saves changes.

                                conn.close()
                                Closes the database.

                        @app.route("/")
                        Connects the / URL to this function. When you open the site in your browser, this is the first page you see.

                        def home():
                        Shows the login page so the user can type a username and password.

                        @app.route("/login", methods=["POST"])
                        Connects the /login URL to this function. When the user clicks the login button, the form data gets sent here to be checked.

                        def login():
                        Handles login.

                                username = request.form["username"]
                                Gets the username that the user typed into the login form.

                                password = request.form["password"]
                                Gets the password that the user typed into the login form.

                                conn = sqlite3.connect("users.db")
                                Opens the database so it can check the login info.

                                cursor = conn.cursor()
                                Sets up a way for the program to talk to the database so it can run the login check.

                                query = "SELECT * FROM users WHERE username=? AND password=?"
                                Is the main fix. Uses placeholders instead of sticking user input right into the SQL command.

                                cursor.execute(query, (username, password))
                                Is the other big fix. Sends the username and password in safely as data instead of letting them change the query.

                                result = cursor.fetchone()
                                Gets one matching row if the login is correct.

                                conn.close()
                                Closes the database.

                                if result:
                                        return "Login successful"
                                Login works.

                                else:
                                        return "Login failed"
                                Login fails.

                        @app.route("/dump")
                        Connects the /dump URL to this function. When you go to this page in the browser, it shows all users in the database.

                        def dump():
                        Handles showing the data from the database.

                                conn = sqlite3.connect("users.db")
                                Opens the database so it can read the data.

                                cursor = conn.cursor()
                                Sets up a way for the program to talk to the database.

                                cursor.execute("SELECT * FROM users")
                                Asks the database for all rows in the users table.

                                rows = cursor.fetchall()
                                Gets all the data returned from the database.

                                conn.close()
                                Closes the database.

                                return str(rows)
                                Sends the data back to the browser so you can see all users.


                Why this is safer:

                        - The query uses placeholders instead of directly adding user input into the SQL command
                        - The username and password are sent in as data, so they cannot change how the query works
                        - SQL injection does not work                





        Reflection:

                In this phase I learned how easy it is to break a login system if the program just trusts what the user types. In the vulnerable version the program takes the username and password and puts it straight into the SQL query. Because of that someone can type special input and change how the query works instead of just logging in normally. That means they could get access without even knowing the real password.

                The secure version showed how a small change can fix a big problem. By using placeholders and sending the input as data the program does not let the user change the SQL command anymore. It just checks if the username and password match like it is supposed to.

                This helped me understand that user input should never be trusted especially when working with databases. Even something that looks simple like a login system can have serious security problems if it is not done the right way. 





Phase 6

This phase is just a menu controller for the project.

Before running, make sure you are in the project folder where main.py is located:
cd "path to your NetSecureToolkit folder"

Then run:
python main.py

Once it starts, just follow the menu and pick what you want to run.

This file does not run the tools itself. It calls netscan.py, which then runs all the features from the other phases.

So this is basically a controller that controls another controller.
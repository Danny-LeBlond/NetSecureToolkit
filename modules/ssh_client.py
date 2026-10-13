# Filename: modules/ssh_client.py

"""
SSH Client Module

This program connects to an SSH server, tries to log in,
runs a command, and shows the output.

Function:
    run_ssh(host, username, password, command)

Parameters:
    host (str): The SSH server
    username (str): Login username
    password (str): Login password
    command (str): Command to run on the server


"""

import paramiko


def run_ssh(host, username, password, command):
    try:
        print("Connecting to SSH server...")
        print("Host:", host)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("Trying to log in...")
        client.connect(host, username=username, password=password, timeout=10)

        print("Connected")
        print()

        print("Running command:", command)
        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode()
        errors = stderr.read().decode()

        print("Output:")
        print(output)

        if errors:
            print("Errors:")
            print(errors)

        client.close()

    except paramiko.AuthenticationException:
        print("Error: bad username or password")

    except Exception as e:
        print("Error:", e)
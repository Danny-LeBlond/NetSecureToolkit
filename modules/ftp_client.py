# Filename: modules/ftp_client.py

"""
FTP Client Module

This program connects to an FTP server, tries to log in,
shows the files on the server and can download a file.

Function:
    run_ftp(host, file_name=None)

Parameters:
    host (str): The FTP server to connect to
    file_name (str): The file to download 

What it does:
    - Connects to an FTP server
    - Tries anonymous login
    - Lists files in the directory
    - Downloads a file if given
"""
from ftplib import FTP

def run_ftp(host, file_name=None):
    try:
        print("Connecting to FTP server...")
        print("Host:", host)

        ftp = FTP(host)
        ftp.set_pasv(True)

        print("Trying anonymous login...")
        ftp.login()

        print("Connected!")
        print()

        print("Changing to pub directory...")
        ftp.cwd("pub")

        print("Files on server:")
        files = ftp.nlst()

        for file in files:
            print(file)

        if file_name:
            print()
            print("Trying to download:", file_name)

            with open(file_name, "wb") as f:
                ftp.retrbinary("RETR " + file_name, f.write)

            print("Download complete!")

        ftp.quit()

    except Exception as e:
        print("Error:", e)
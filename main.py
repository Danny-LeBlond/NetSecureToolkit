"""
Main Menu Controller (Phase 6)

This file is a menu-based controller for the NetSecure Toolkit.
It does not implement the tools itself.

What it does:
- Shows a menu for each phase (1-5)
- Takes user input and routes it to the correct feature
- Calls netscan.py with the right arguments using subprocess

How it works:
main.py (this file) = menu controller
netscan.py = argument-based controller
modules = actual tool implementations

So this file is basically a controller controlling another controller (netscan.py)
"""


import argparse
import logging
import subprocess
import sys
import time
import os

logging.basicConfig(
    filename="netsecure_toolkit_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def print_section_header(section_title):
    print("\n" + "=" * 50)
    print(section_title)
    print("=" * 50)


def run_http_client_menu():
    print_section_header("HTTP Client")
    print("1. Connect to example.com")
    print("2. Connect to https://example.com")
    print("3. Enter your own website")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        user_host_input = "example.com"
    elif choice == "2":
        user_host_input = "https://example.com"
    elif choice == "3":
        user_host_input = input("Enter website: ").strip()
    else:
        print("Invalid choice")
        return

    logging.info("HTTP Client started for host: %s", user_host_input)
    netscan_path = os.path.join(os.path.dirname(__file__), "netscan.py")
    project_folder = os.path.dirname(__file__)
    subprocess.run([sys.executable, netscan_path, "--http", user_host_input], cwd=project_folder)
    


def run_port_scanner_menu():
    print_section_header("Port Scanner")
    print("1. Scan localhost (127.0.0.1) ports 1-100")
    print("2. Enter your own host and port range")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        target_host = "127.0.0.1"
        port_range_input = "1-100"
    elif choice == "2":
        target_host = input("Enter host to scan (example.com or 127.0.0.1): ").strip()
        port_range_input = input("Enter port range like 1-100: ").strip()
    else:
        print("Invalid choice")
        return

    logging.info("Port scan started for %s ports %s", target_host, port_range_input)
    netscan_path = os.path.join(os.path.dirname(__file__), "netscan.py")
    project_folder = os.path.dirname(__file__)
    subprocess.run([sys.executable, netscan_path, "--scan", target_host, "--ports", port_range_input], cwd=project_folder)


def run_ftp_client_menu():
    print_section_header("FTP Interaction")
    print("What this does: connects to a File Transfer Protocol (FTP) server and shows files.")
    print("It can also download a file if you give one.")
    print()
    print("1. Demo: connect to ftp.cs.brown.edu and list files")
    print("   - Uses a public FTP server")
    print("   - Logs in with anonymous login (no username/password needed)")
    print("   - Shows files in the public folder")
    print()
    print("2. Enter your own FTP server")
    print("   - Server: the FTP server you want to connect to")
    print("   - You can try downloading a file if the server allows it")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        print()
        print("Running demo: connecting to ftp.cs.brown.edu and listing files...")
        ftp_host_input = "ftp.cs.brown.edu"
    elif choice == "2":
        print()
        print("Enter your own FTP server below.")
        ftp_host_input = input("Enter FTP server (example.com): ").strip()
        if ftp_host_input == "":
            print("Error: FTP server cannot be empty")
            return

    else:
        print("Invalid choice")
        return

    ftp_file_input = input("Enter file to download or press Enter to skip: ").strip()

    print()
    print("Connecting to FTP server and getting data...")

    if ftp_file_input == "":
        netscan_path = os.path.join(os.path.dirname(__file__), "netscan.py")
        project_folder = os.path.dirname(__file__)
        subprocess.run([sys.executable, netscan_path, "--ftp", ftp_host_input], cwd=project_folder)
    else:
        netscan_path = os.path.join(os.path.dirname(__file__), "netscan.py")
        project_folder = os.path.dirname(__file__)
        subprocess.run([sys.executable, netscan_path, "--ftp", ftp_host_input, "--download", ftp_file_input], cwd=project_folder)


def run_ssh_client_menu():
    print_section_header("SSH Interaction")
    print("What this does: connects to a server using SSH and runs a command on that server.")
    print()
    print("1. Demo: connect to test.rebex.net and run a command (ls)")
    print("   - Uses a public test server")
    print("   - Logs in with demo credentials")
    print("   - Runs a command and shows the output")
    print()
    print("2. Enter your own SSH server")
    print("   - Server: the computer you want to connect to")
    print("   - Username/Password: login for that server")
    print("   - Command: something to run like 'ls' or 'whoami'")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        print()
        print("Running demo: connecting to test.rebex.net and listing files...")
        ssh_host_input = "test.rebex.net"
        ssh_username_input = "demo"
        ssh_password_input = "password"
        ssh_command_input = "ls"
    elif choice == "2":
        print()
        print("Enter your own connection info below.")
        ssh_host_input = input("Enter SSH server (example.com or IP): ").strip()
        ssh_username_input = input("Enter username: ").strip()
        ssh_password_input = input("Enter password: ").strip()
        ssh_command_input = input("Enter command to run (ex: ls, whoami): ").strip()

        if not ssh_host_input or not ssh_username_input or not ssh_password_input or not ssh_command_input:
            print("Error: all fields are required")
            return
    else:
        print("Invalid choice")
        return

    print()
    print("Connecting and running command...")

    netscan_path = os.path.join(os.path.dirname(__file__), "netscan.py")
    project_folder = os.path.dirname(__file__)
    subprocess.run([
        sys.executable,
        netscan_path,
        "--ssh", ssh_host_input,
        "--user", ssh_username_input,
        "--password", ssh_password_input,
        "--command", ssh_command_input
    ], cwd=project_folder)


def run_phase_three_menu():
    while True:
        print_section_header("Phase 3 - File Transfer Protocol and Secure Shell")
        print("1. File Transfer Protocol (FTP) Interaction")
        print("2. Secure Shell (SSH) Interaction")
        print("3. Back to Main Menu")
        phase_three_menu_choice = input("Choose an option: ").strip()

        if phase_three_menu_choice == "1":
            run_ftp_client_menu()
        elif phase_three_menu_choice == "2":
            run_ssh_client_menu()
        elif phase_three_menu_choice == "3":
            break
        else:
            print("Invalid choice")


def run_sql_injection_menu():
    while True:
        print_section_header("SQL Injection Demo")
        print("1. Run Vulnerable SQL Demo")
        print("2. Run Secure SQL Demo")
        print("3. Back to Main Menu")

        sql_menu_choice = input("Choose an option: ").strip()
        project_folder = os.path.dirname(__file__)
        netscan_path = os.path.join(project_folder, "netscan.py")

        if sql_menu_choice == "1":
            subprocess.run([sys.executable, netscan_path, "--sqlvuln"], cwd=project_folder)
        elif sql_menu_choice == "2":
            subprocess.run([sys.executable, netscan_path, "--sqlsecure"], cwd=project_folder)
        elif sql_menu_choice == "3":
            break
        else:
            print("Invalid choice")


def show_phase_four_information():
    print_section_header("Phase 4 - Vulnerability Analysis")
    print("This section is from Phase 4 of the project.")
    print("It is NOT something you run like the other options.")
    print()
    print("Phase 4 was about finding and fixing security problems in code.")
    print("That work is written and explained in the docs folder.")
    print()
    print("Go to this folder to see it:")
    print("NetSecureToolkit/docs/Phase 4")
    print()
    time.sleep(5)


def show_main_menu():
    while True:
        print_section_header("NetSecure Toolkit")
        print("1. HTTP Client (Phase 1)")
        print("2. Port Scanner (Phase 2)")
        print("3. File Transfer Protocol and Secure Shell (Phase 3)")
        print("4. Phase 4 Vulnerability Analysis")
        print("5. SQL Injection Demo (Phase 5)")
        print("6. Exit")
        main_menu_choice = input("Choose an option: ").strip()

        if main_menu_choice == "1":
            run_http_client_menu()
        elif main_menu_choice == "2":
            run_port_scanner_menu()
        elif main_menu_choice == "3":
            run_phase_three_menu()
        elif main_menu_choice == "4":
            show_phase_four_information()
        elif main_menu_choice == "5":
            run_sql_injection_menu()
        elif main_menu_choice == "6":
            print("Exiting NetSecure Toolkit.")
            logging.info("Program exited")
            break
        else:
            print("Invalid choice")


def main():
    parser = argparse.ArgumentParser(description="NetSecure Toolkit Main Menu")
    parser.add_argument("--menu", action="store_true")
    args = parser.parse_args()
    show_main_menu()


if __name__ == "__main__":
    main()

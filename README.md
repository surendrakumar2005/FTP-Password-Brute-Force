# FTP Password Brute-Force Script (Educational Use Only)

This is a multithreaded FTP password checking tool written in Python. Important: Use this only on servers you own or have explicit permission to test. The script demonstrates multithreaded password attempts using ThreadPoolExecutor, supports a file-based wordlist or a built-in list of top 100 common passwords, allows customisation of host, username, port, and number of threads, provides friendly terminal output with coloured messages using colorama, and automatically stops threads once the password is found.

Requirements: Python 3.7+ and the colorama library. Install colorama with `pip install colorama`.

To run the script, use:
```bash
python ftp_bruteforce.py -H <host> -u <username> [-p <wordlist>] [-t <threads>] [-port <port>]

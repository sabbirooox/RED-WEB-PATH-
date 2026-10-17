import requests
import threading
import os
import sys
import time

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install colorama requests")
    from colorama import Fore, Style, init
    init(autoreset=True)

target_url = ""
wordlist = ["admin", "login", "backup", "config", "robots.txt", "dashboard", "api", "uploads", "images"]

def scan_path(path):
    global target_url
    url = f"{target_url}/{path}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 404:
            print(Fore.GREEN + f"[*] Found: {url} | Status: {response.status_code} | Size: {len(response.content)}")
        else:
            print(Fore.RED + f"[-] Not Found: {url}")
    except requests.exceptions.RequestException:
        pass 

def start_scan():
    global target_url
    target_url = input(Fore.WHITE + "Enter Target URL (e.g., http://testphp.vulnweb.com): ").strip()
    if not target_url.startswith("http"): target_url = "http://" + target_url
    print(Fore.CYAN + f"\n[*] Scanning {target_url}...")
    threads = []
    for path in wordlist:
        t = threading.Thread(target=scan_path, args=(path,))
        threads.append(t)
        t.start()
    for thread in threads: thread.join()
    input(Fore.YELLOW + "\nPress Enter to exit...")

os.system('clear')
print(Fore.RED + """
██████╗ ███████╗██████╗     ██╗    ██╗███████╗██████╗     ██████╗  █████╗ ████████╗██╗  ██╗
██╔══██╗██╔════╝██╔══██╗    ██║    ██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝██║  ██║
██████╔╝█████╗  ██║  ██║    ██║ █╗ ██║█████╗  ██████╔╝    ██████╔╝███████║   ██║   ███████║
██╔══██╗██╔══╝  ██║  ██║    ██║███╗██║██╔══╝  ██╔══██╗    ██╔═══╝ ██╔══██║   ██║   ██╔══██║
██║  ██║███████╗██████╔╝    ╚███╔███╔╝███████╗██████╔╝    ██║     ██║  ██║   ██║   ██║  ██║
╚═╝  ╚═╝╚══════╝╚═════╝      ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
""")
print(Fore.MAGENTA + "                          DEVELOPER BY SABBIR ØX")
print(Fore.RED + "-------------------------------------------------------------------------------------")
start_scan()

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
# আপনার প্রয়োজন অনুযায়ী ওয়ার্ডলিস্ট বাড়াতে পারেন
wordlist = [
    "admin", "login", "backup", "config", "robots.txt", "dashboard", 
    "api", "uploads", "images", "db", "test", "dev", "wp-admin", 
    "phpmyadmin", "server-status", "secret", "hidden", "cgi-bin"
]

def scan_path(path):
    global target_url
    url = f"{target_url}/{path}"
    try:
        # রিকোয়েস্ট পাঠানো হচ্ছে
        response = requests.get(url, timeout=3)
        
        # স্ট্যাটাস কোড অনুযায়ী কালার এবং মেসেজ সিলেক্ট করা
        if response.status_code == 200:
            print(Fore.GREEN + f"[+] FOUND: {url} | Status: 200 OK | Size: {len(response.content)} bytes")
        elif response.status_code == 403:
            print(Fore.YELLOW + f"[!] FORBIDDEN: {url} | Status: 403 | Size: {len(response.content)} bytes")
        elif response.status_code == 301 or response.status_code == 302:
            print(Fore.CYAN + f"[*] REDIRECT: {url} | Status: {response.status_code} | Size: {len(response.content)} bytes")
        else:
            # 404 বা অন্যান্য এরর হলেও দেখাবে
            print(Fore.RED + f"[-] NOT FOUND: {url} | Status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(Fore.MAGENTA + f"[X] ERROR: {url} | Connection Failed")

def start_scan():
    global target_url
    print(Fore.YELLOW + "\n[*] Enter Target URL (e.g., http://testphp.vulnweb.com)")
    target_url = input(Fore.WHITE + "Target: ").strip()
    
    # http:// বা https:// না থাকলে যোগ করে দেওয়া
    if not target_url.startswith("http"):
        target_url = "http://" + target_url
    
    print(Fore.CYAN + f"\n[*] Scanning {target_url} for hidden directories...")
    print(Fore.RED + "-------------------------------------------------------------------------------------")
    time.sleep(1)

    threads = []
    for path in wordlist:
        t = threading.Thread(target=scan_path, args=(path,))
        threads.append(t)
        t.start()
        
    for thread in threads:
        thread.join()

    print(Fore.RED + "-------------------------------------------------------------------------------------")
    print(Fore.GREEN + "[✓] Scan Complete!")
    input(Fore.YELLOW + "\nPress Enter to return to menu...")

def main():
    while True:
        os.system('clear')
        banner = """
██████╗ ███████╗██████╗     ██╗    ██╗███████╗██████╗     ██████╗  █████╗ ████████╗██╗  ██╗
██╔══██╗██╔════╝██╔══██╗    ██║    ██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝██║  ██║
██████╔╝█████╗  ██║  ██║    ██║ █╗ ██║█████╗  ██████╔╝    ██████╔╝███████║   ██║   ███████║
██╔══██╗██╔══╝  ██║  ██║    ██║███╗██║██╔══╝  ██╔══██╗    ██╔═══╝ ██╔══██║   ██║   ██╔══██║
██║  ██║███████╗██████╔╝    ╚███╔███╔╝███████╗██████╔╝    ██║     ██║  ██║   ██║   ██║  ██║
╚═╝  ╚═╝╚══════╝╚═════╝      ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
        """
        print(Fore.RED + Style.BRIGHT + banner)
        print(Fore.MAGENTA + Style.BRIGHT + "                          DEVELOPER BY SABBIR ØX")
        print(Fore.RED + "-------------------------------------------------------------------------------------")
        print(Fore.CYAN + "[1] " + Fore.WHITE + "START WEB PATH SCAN")
        print(Fore.RED + "[2] " + Fore.WHITE + "EXIT")
        print(Fore.RED + "-------------------------------------------------------------------------------------")
        
        choice = input(Fore.YELLOW + "\nSelect an option: " + Fore.WHITE)
        
        if choice == '1':
            start_scan()
        elif choice == '2':
            print(Fore.RED + "Exiting... Goodbye!")
            sys.exit()
        else:
            print(Fore.RED + "Invalid option!")
            time.sleep(1)

if __name__ == "__main__":
    main()

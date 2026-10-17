#!/bin/bash
clear
echo -e "\e[1;32m[+] Installing Requirements...\e[0m"
pkg update -y && pkg upgrade -y
pkg install python -y
pip install colorama requests

echo -e "\e[1;32m[+] Downloading RED WEB PATH Tool...\e[0m"
curl -sL https://raw.githubusercontent.com/sabbirooox/RED-WEB-PATH-/main/webpath.py -o webpath.py

chmod +x webpath.py

echo -e "\e[1;34m[✓] Installation Complete!\e[0m"
echo -e "\e[1;33mType 'python webpath.py' to run the tool.\e[0m"

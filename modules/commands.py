import requests
import sys
import json
from colorama import Fore, Back, Style
import os

def command(syA2, syA1):
   print("##################################### \n")
   if syA2 == '--nmap' or syA2 == '-n':
      print('--------------------------   -------------------------------------------')
      print("If Nmap is slow to respond don't worry, sometimes it takes a while.")
      print('--------------------------------------------------------------------- \n \n')
      ip = syA1
      nmapcc = os.system('nmap ' + ip)
      print(nmapcc)
      sys.exit(0)

   else:
      print('Review the command after the IP, \nwrite python geo-recon.py --command or -c to see the avaliables commands')
   print("\n##################################### \n")


def listCommand():
      print(Fore.WHITE+'# Commands')
      print('python geo-recon.py --help or -h                   (Display help)')
      print('python geo-recon.py 138.121.128.19 --nmap or -n    (Nmap standard use)')
      print('python geo-recon.py 138.121.128.19                 (Standard use, infos about IP)')
      print('python geo-recon.py --commands or -c               (Display commands availables )') 

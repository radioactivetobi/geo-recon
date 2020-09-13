import requests
import sys
import json
from colorama import Fore, Back, Style
import os


def myIp():
    r = requests.get('https://api.myip.com')
    response = json.loads(r.text)
    ip = (response["ip"])
    return ip


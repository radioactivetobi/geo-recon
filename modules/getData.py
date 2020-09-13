import requests
import sys
import json
from colorama import Fore, Back, Style
import os

def getGeo(syA1):
    r = requests.get('http://ip-api.com/json/'+syA1)
    response = json.loads(r.text)

    #Iterate the data, filter & print ( data for specific fields
    print ( "\n" + Fore.YELLOW + "[*] Running Geo-location Check Against"+ " " + sys.argv[1] + "\n") 
    print ( Fore.WHITE + "Country: "+ response["country"])
    print ( "Region: " + response["regionName"])
    print ( "City: " + response["city"])
    print ( "Organization: "+response["org"])
    print ( "Longitude: ", response["lon"])
    print ( "Latitude: ", response["lat"])
    print ( "ISP: "+ response["isp"] + "\n") 
    print ( Fore.GREEN + "[*] Geo-IP Lookup Complete!!!" + "\n")
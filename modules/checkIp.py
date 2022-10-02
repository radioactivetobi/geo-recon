import requests
import sys
import json
from colorama import Fore, Back, Style
import os

def check(syA1):
    print ( "\n" + Fore.YELLOW + "[*] Running Reputation Check Against"+ " ", syA1 + "\n")

    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': syA1,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': '58878ed65228db88eddfda4983bce5d19d425ddf81f427857b3f59f11aecc34f127862a1cc7d4581'
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
 
    # Formatted output
    decodedResponse = json.loads(response.text)
    
    try:
        errors = [error['detail'] for error in decodedResponse['errors']]
        print ( Fore.RED + "Errors:\n    " + "\n    ".join(errors) + Fore.RESET + "\n\n")
        return 1
    except:
        pass
    
    print ( Fore.WHITE + "Domain: " + json.dumps(decodedResponse ["data"]["domain"]))
    print ( "Hostname: " + json.dumps(decodedResponse ["data"]["hostnames"]))
    print ( "Usage Type: " + json.dumps(decodedResponse ["data"]["usageType"]))
    print ( "Confidence of Abuse: " + json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]))
    print ( "Number Times of Reported: " + json.dumps(decodedResponse ["data"]["totalReports"]))
    print ( "Last Reported: " + json.dumps(decodedResponse ["data"]["lastReportedAt"]))
    print ( "Whitelisted: " + json.dumps(decodedResponse ["data"]["isWhitelisted"]) + "\n")

    #This conditional statement outputs the status of the ip address based on abuse of confidence
    if json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "100":
        print ( Fore.YELLOW + "The IP Address " + sys.argv[1] + " Is Malicious and well known for SSH Bruteforce Attacks" + "\n")
    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "0":
        print ( Fore.GREEN + "The IP Address " + sys.argv[1] + " Is Not Malicious" + "\n")
    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) < "20":
        print ( "The IP Address " + sys.argv[1] + " Is Probably Not Malicious But Should Be Investigated Further")
    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) <= "20":
        print ( "The IP Address " + sys.argv[1] + " Is Probably Malicious And Should Be Investigated Further")
    else:
        print ( "[*] IP Reputation Look up Complete!!!" + "\n" )

    print ( Fore.GREEN + "[*] IP Reputation Look up Complete!!!" + "\n" )
    print ( Fore.RESET )
import requests
import sys
import json
from colorama import Fore, Back, Style 

f = open("header.txt", "r")
print(f.read())

if len(sys.argv) < 2:
   print (Fore.GREEN + " Usage: " + "python geo-recon.py <ipaddress>")
   sys.exit(1)
#if sys.argv == "-h":
   #print " Usage: " + "python geo-recon.py <ipaddress>"
   #print " Example: " + "python geo-recon.py 192.168.24.72"
   #sys.exit(1)

#Get geo data for supplied ip address
address = sys.argv[1]
r = requests.get('http://ip-api.com/json/'+address)
response = json.loads(r.text)

#Iterate the data, filter & print data for specific fields
print "\n" + Fore.YELLOW + "[*] Running Geo-location Check Against"+ " " + sys.argv[1] + "\n" 
print Fore.WHITE + "Country: "+ response["country"]
print "Region: " + response["regionName"]
print "City: " + response["city"]
print "Organization: "+response["org"]
#print "Longitude: "+ response["lon"]
#print "Latitude: "+ response["lat"]
print "ISP: "+ response["isp"] + "\n" 
print Fore.GREEN + "[*] Geo-IP Lookup Complete!!!" + "\n"



# Check IP reputation information


print "\n" + Fore.YELLOW + "[*] Running Reputation Check Against"+ " " + sys.argv[1] + "\n"

url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': address,
    'maxAgeInDays': '90'
}

headers = {
    'Accept': 'application/json',
    'Key': '58878ed65228db88eddfda4983bce5d19d425ddf81f427857b3f59f11aecc34f127862a1cc7d4581'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)
print Fore.WHITE + "Domain: " + json.dumps(decodedResponse ["data"]["domain"])
print "Hostname: " + json.dumps(decodedResponse ["data"]["hostnames"])
print "Usage Type: " + json.dumps(decodedResponse ["data"]["usageType"])
print "Confidence of Abuse: " + json.dumps(decodedResponse ["data"]["abuseConfidenceScore"])
print "Number Times of Reported: " + json.dumps(decodedResponse ["data"]["totalReports"])
print "Last Reported: " + json.dumps(decodedResponse ["data"]["lastReportedAt"])
print "Whitelisted: " + json.dumps(decodedResponse ["data"]["isWhitelisted"]) + "\n"

#This conditional statement outputs the status of the ip address based on abuse of confidence
if json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "100":
   print Fore.YELLOW + "The IP Address " + sys.argv[1] + " Is Malicious and well known for SSH Bruteforce Attacks" + "\n"
elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "0":
   print Fore.GREEN + "The IP Address " + sys.argv[1] + " Is Not Malicious" + "\n"
elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) < "20":
   print "The IP Address " + sys.argv[1] + " Is Probably Not Malicious But Should Be Investigated Further"
elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) > "20":
   print "The IP Address " + sys.argv[1] + " Is Probably Malicious And Should Be Investigated Further"
else:
   print "[*] IP Reputation Look up Complete!!!" + "\n" 

print Fore.GREEN + "[*] IP Reputation Look up Complete!!!" + "\n" 

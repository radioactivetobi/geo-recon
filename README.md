# Geo-Recon
An OSINT CLI tool desgined to fast track IP Reputation and Geo-locaton look up for Security Analysts.

# Setup
This tool is compactible with:
* Any Linux Operating System (Debian, Ubuntu, CentOS)
* Termux

# Linux Setup
```bash
git clone https://github.com/radioactivetobi/geo-recon.git
cd geo-recon
chmod +x geo-recon.py
pip install -r requirements.txt
```
# Termux Setup
```bash
git clone https://github.com/radioactivetobi/geo-recon.git
cd geo-recon
chmod +x geo-recon.py
pip install -r requirements.txt
```
# Sample Syntax Linux
```bash
root@kali:~/geo-recon# python geo-recon.py 138.121.128.19

░██████╗░███████╗░█████╗░  ██████╗░███████╗░█████╗░░█████╗░███╗░░██╗
██╔════╝░██╔════╝██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║
██║░░██╗░█████╗░░██║░░██║  ██████╔╝█████╗░░██║░░╚═╝██║░░██║██╔██╗██║
██║░░╚██╗██╔══╝░░██║░░██║  ██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║╚████║
╚██████╔╝███████╗╚█████╔╝  ██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚███║
░╚═════╝░╚══════╝░╚════╝░  ╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚══╝

                         By d3xt3r_182
 Github: https://github.com/radioactivetobi | Twitter: @d3xt3r_182
            Usage: python geo-recon.py <IPADDRESS> 
            


[*] Running Geo-location Check Against 138.121.128.19

Country: Brazil
Region: Piaui
City: Teresina
Organization: Itech Telecom
ISP: Itech Telecom

[*] Geo-IP Lookup Complete!!!


[*] Running Reputation Check Against 138.121.128.19

Domain: "redeitechtelecom.com.br"
Hostname: []
Usage Type: "Fixed Line ISP"
Confidence of Abuse: 100
Number Times of Reported: 982
Last Reported: "2020-08-21T16:43:12+00:00"
Whitelisted: false

The IP Address 138.121.128.19 Is Malicious and well known for SSH Bruteforce Attacks

[*] IP Reputation Look up Complete!!!
```
# Sample Syntax Termux
```bash
$ python2 geo-recon.py 138.121.128.19

░██████╗░███████╗░█████╗░  ██████╗░███████╗░█████╗░░█████╗░███╗░░██╗
██╔════╝░██╔════╝██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║
██║░░██╗░█████╗░░██║░░██║  ██████╔╝█████╗░░██║░░╚═╝██║░░██║██╔██╗██║
██║░░╚██╗██╔══╝░░██║░░██║  ██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║╚████║
╚██████╔╝███████╗╚█████╔╝  ██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚███║
░╚═════╝░╚══════╝░╚════╝░  ╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚══╝

                         By d3xt3r_182
 Github: https://github.com/radioactivetobi | Twitter: @d3xt3r_182
            Usage: python geo-recon.py <IPADDRESS> 
            


[*] Running Geo-location Check Against 138.121.128.19

Country: Brazil
Region: Piaui
City: Teresina
Organization: Itech Telecom
ISP: Itech Telecom

[*] Geo-IP Lookup Complete!!!


[*] Running Reputation Check Against 138.121.128.19

Domain: "redeitechtelecom.com.br"
Hostname: []
Usage Type: "Fixed Line ISP"
Confidence of Abuse: 100
Number Times of Reported: 982
Last Reported: "2020-08-21T16:43:12+00:00"
Whitelisted: false

The IP Address 138.121.128.19 Is Malicious and well known for SSH Bruteforce Attacks

[*] IP Reputation Look up Complete!!!
```
# To Do List
* [ ] Include Longitude & Latitude For Geo-IP Lookup
* [ ] Fix API


#!/bin/bash
nmap --version > /dev/null 2>&1
if [ "$?" = "0" ]; then
    exit 1

else
    echo Is necessary to install Nmap, instaling...
    sudo apt install nmap -y > /dev/null 2>&1

fi

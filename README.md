# Block-Websites-with-python
It's a websites blocker program.
## Requirements
I used the time and Datetime Module only which comes by default with the Python Standard Library 
therefore you don’t need to install anything.
## What about hosts ?
Every operating system has a host file and it’s on this file where I added a list of websites 
I wanted to block by redirecting them to 127.0.0.1 (localhost).

## What the program does ?
We will add website URLs to the host file and mapping them to the localhost thus preventing you 
from accessing the real site during working hours.

## Location of host file
- For those in Linux:
``` Linux_host = "/etc/hosts" ```
- For those in window:
``` Window_host = r"C:\Windows\System32\drivers\etc\hosts" ```

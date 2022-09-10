import ipinfo
import sys

#Obtain the IP Address from the Command Line
try:
    ip_address = sys.argv[1]
except IndexError:
    ip_address = None

#Input the access toke from ipinfo.io
access_token = 'Import Your Token Here'
#Create a client object with the provided access token
handler = ipinfo.getHandler(access_token)
#Obtain the IP information
details = handler.getDetails(ip_address)
#Print the obtained information
for key, value in details.all.items():
    print(f"{key}: {value}")

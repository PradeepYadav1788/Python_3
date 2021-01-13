import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <URL>" )
    sys.exit(1)

req = requests.get("https://"+sys.argv[1])
print("\n " + str(req.headers))

gatherhostby = socket.gethostbyname(sys.argv[1])

#print(str(gatherhostby))
print("\nThe iP address of "+sys.argv[1]+" is: "+gatherhostby+"\n")

#print("\nThe iP address of{0}is {1}\n".format(sys.argv[1], gatherhostby))

# ipinfo.io is is helpful to get the details
req_two = requests.get("https://ipinfo.io/"+gatherhostby+"/json")

resp = json.loads(req_two.text)
print("\n" +str(req.headers['server']))
print("Location : "+resp['loc'])
print("Rigion : "+resp['region'])
print("City : "+resp['city'])
print("Country : "+resp['country'])

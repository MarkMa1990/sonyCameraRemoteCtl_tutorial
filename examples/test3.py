import sys
import socket

SSDP_ADDR = "239.255.255.250";
SSDP_PORT = 1900;
SSDP_MX = 1;
SSDP_ST = "urn:schemas-sony-com:service:ScalarWebAPI:1";

ssdpRequest = "M-SEARCH * HTTP/1.1\r\n" + \
                "HOST: %s:%d\r\n" % (SSDP_ADDR, SSDP_PORT) + \
                "MAN: \"ssdp:discover\"\r\n" + \
                "MX: %d\r\n" % (SSDP_MX, ) + \
                "ST: %s\r\n" % (SSDP_ST, ) + "\r\n";

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)
try:
    sock.sendto(ssdpRequest.encode(), (SSDP_ADDR, SSDP_PORT))
    print (sock.recv(1000).decode())
except:
    None

# from test1.py we found the Device descriptions of Sony \alpha 6000

HOST="192.168.122.1"
PORT=61000

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.settimeout(2)
sock2.connect((HOST, PORT))
ssdpRequest2 =  "GET /scalarwebapi_dd.xml HTTP/1.1\r\n" +\
                "Host: http://192.168.122.1:61000\r\n" + \
                "Connection: close\r\n" + \
                "Accept: */*\r\n\r\n" # I checked that camera uses Fedora, it accepts \r\n as the new line comamnd, \n seems not working when send the request
try:
    # send binary to the server
    sock2.send(ssdpRequest2.encode())
    # receive once
    res0 = sock2.recv(1024).decode()
    # receive a few times until the server stops sending data
    while(len(res0)>0):
        print (res0)
        res0 = sock2.recv(1024).decode()
except:
    print ("received Nothing")


print ('------END OF PART 2-------')





# part 3
HOST2="192.168.122.1"
PORT2=8080


#sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock2.settimeout(2)
#sock2.connect((HOST2, PORT2))
ssdpRequest2 = "POST /sony/camera HTTP/1.1\r\n" +\
               "Host: 192.168.122.1:8080\r\n" +\
               "User-Agent: python-request\r\n" +\
               "Accept-Encoding: gzip, deflate\r\n" +\
               "Accept: */*\r\n" +\
               "Connection: keep-alive\r\n"
               #"Content-Length: %s\r\n\r\n" %len(json.dumps(js_startReMode)) # this line must be included, telling the server of the json length
               

js_startReMode = {
        "method":"startRecMode",
        "params":[],
        "id": 1,
        "version": "1.0"
        }
        
js_getSuppMode = {
        "method":"getSupportedShootMode",
        "params":[],
        "id": 1,
        "version": "1.0"
        }

js_actTkPhoto = {
        "method":"actTakePicture",
        "params":[],
        "id": 1,
        "version": "1.0"
        }
        

import json
        

try:
    print ('-------------START REMOTE CONTROL-------------')
    # send "startRecMode" request to camera
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock2.settimeout(10)
    sock2.connect((HOST2, PORT2))
    
    strAll = ssdpRequest2 + "Content-Length: %s\r\n\r\n" %len(json.dumps(js_startReMode)) + json.dumps(js_startReMode)
    print (strAll)
    sock2.send(bytearray(strAll,'utf-8'))    
    
    print ('setRemote')
    res0 = sock2.recv(1024)
    while(len(res0)>0):
        print (res0)
        res0 = sock2.recv(1024)
    
    sock2.close()
    sock2 = None
    print ('--------------------------------------')
    print ('')
    
    # send "actTakePicture" request to camera (take a photo)
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock2.settimeout(10)
    sock2.connect((HOST2, PORT2))
    
    strAll = ssdpRequest2 + "Content-Length: %s\r\n\r\n" %len(json.dumps(js_actTkPhoto)) + json.dumps(js_actTkPhoto)
    print (strAll)
    sock2.send(bytearray(strAll,'utf-8'))
    
    print ('getSupportedMode')
    res0 = sock2.recv(1024)
    while(len(res0)>0):
        print (res0)
        res0 = sock2.recv(1024)
        
    
    sock2.close()
    sock2 = None
        
except:
    print ("Something wrong here")



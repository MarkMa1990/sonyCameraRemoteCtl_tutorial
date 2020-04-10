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

# sonyCameraRemoteCtl_tutorial
example of Sony camera remote Ctl

Here, I am using Sony \alpha 6000 for tests. The outcome for other cameras can be different.

## example 1
Run example 1:

```shell
python3 test1.py
```
I get responses like this:

```html
HTTP/1.1 200 OK
CACHE-CONTROL: max-age=1800
EXT: 
LOCATION: http://192.168.122.1:61000/scalarwebapi_dd.xml
SERVER: FedoraCore/2 UPnP/1.0 MINT-X/1.8.1
ST: urn:schemas-sony-com:service:ScalarWebAPI:1
USN: uuid:000000001000-1010-8000-8E45007C0641::urn:schemas-sony-com:service:ScalarWebAPI:1
```

## example 2
Run example 2:

```shell
python3 test2.py
```
results are like this:

```html
HTTP/1.1 200 OK
CACHE-CONTROL: max-age=1800
EXT: 
LOCATION: http://192.168.122.1:61000/scalarwebapi_dd.xml
SERVER: FedoraCore/2 UPnP/1.0 MINT-X/1.8.1
ST: urn:schemas-sony-com:service:ScalarWebAPI:1
USN: uuid:000000001000-1010-8000-8E45007C0641::urn:schemas-sony-com:service:ScalarWebAPI:1


HTTP/1.1 200 OK
Accept-Range: none
Content-Length: 2139
Content-Type: text/xml; charset="utf-8"
Connection: close
Date: Thu, 01 Jan 1970 01:35:40 GMT
Server: FedoraCore/2 UPnP/1.0 MINT-X/1.8.1


<?xml version="1.0"?>
<root xmlns="urn:schemas-upnp-org:device-1-0">
  <specVersion>
    <major>1</major>
    <minor>0</minor>
  </specVersion>
  <device>
    <deviceType>urn:schemas-upnp-org:device:Basic:1</deviceType>
    <friendlyName>ILCE-6000</friendlyName>
    <manufacturer>Sony Corporation</manufacturer>
    <manufacturerURL>http://www.sony.net/</manufacturerURL>
    <modelDescription>SonyDigitalMediaServer</modelDescription>
    <modelName>SonyImagingDevice</modelName>
    <UDN>uuid:000000001000-1010-8000-8E45007C0641</UDN>
    <serviceList>
      <service>
        <serviceType>urn:schemas-sony-com:service:ScalarWebAPI:1</serviceType>
        <serviceId>urn:schemas-sony-com:serviceId:ScalarWebAPI</serviceId>
        <SCPDURL></SCPDURL>
        <controlURL></controlURL>
        <eventSubURL></eventSubURL>
      </service>
    </serviceList>
    <av:X_ScalarWebAPI_DeviceInfo xmlns:av="urn:schemas-sony-com:av">
      <av:X_ScalarWebAPI_Version>1.0</av:X_ScalarWebAPI_Version>
      <av:X_ScalarWebAPI_Serv
iceList>
        <av:X_ScalarWebAPI_Service>
          <av:X_ScalarWebAPI_ServiceType>guide</av:X_ScalarWebAPI_ServiceType>
          <av:X_ScalarWebAPI_ActionList_URL>http://192.168.122.1:8080/sony</av:X_ScalarWebAPI_ActionList_URL>
          <av:X_ScalarWebAPI_AccessType></av:X_ScalarWebAPI_AccessType>
        </av:X_ScalarWebAPI_Service>
        <av:X_ScalarWebAPI_Service>
          <av:X_ScalarWebAPI_ServiceType>accessControl</av:X_ScalarWebAPI_ServiceType>
          <av:X_ScalarWebAPI_ActionList_URL>http://192.168.122.1:8080/sony</av:X_ScalarWebAPI_ActionList_URL>
          <av:X_ScalarWebAPI_AccessType></av:X_ScalarWebAPI_AccessType>
        </av:X_ScalarWebAPI_Service>
        <av:X_ScalarWebAPI_Service>
          <av:X_ScalarWebAPI_ServiceType>camera</av:X_ScalarWebAPI_ServiceType>
          <av:X_ScalarWebAPI_ActionList_URL>http://192.168.122.1:8080/sony</av:X_ScalarWebAPI_ActionList_URL>
          <av:X_ScalarWebAPI_AccessType></av:X_ScalarWebAPI_AccessType>
        </av:X_ScalarWebAPI_Service>
    
  </av:X_ScalarWebAPI_ServiceList>
    </av:X_ScalarWebAPI_DeviceInfo>
  </device>
</root>


```


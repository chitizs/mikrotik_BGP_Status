# Mikrotik_BGP_Status
BGP status of Mikrotik(MK) Devices

This project deals with Generating Alert for BGP status of Mikrotik Routers.

Mikrotik RouterOS, upto time of this writing, has not provided BGP-status OIDS. 
To circumvent this, a script is written(and will be hosted in a linux server).

This will gather BGP status for all MK routers. Also, an Inventory file with IP address of BGP routers is populated. 
SNMP poller(NMS) will poll this Server using extended oid(1.3.6.1.4.1.8072.1.3.1).
After this server will execute the script and reply to NMS server with BGP peers status. 
The scripts uses python librouteros API to execute BGP command('/routing/bgp/peer/print'). 

If everything is OK (ie All bgp peer is established), 1 will be returned.
If there is a problem then info about the problematic peers is/are returned.
Note, install librouteros library using "pip3 install librouteros"


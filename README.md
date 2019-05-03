# Mikrotik_BGP_Status
BGP status of Mikrotik(MK) Devices

This project deals with Generating Alert for BGP status of Mikrotik Routers.

Mikrotik RouterOS, upto time of this writing, has not provided BGP-status OIDS. 
To curcumvent this, a script is written(hosted in a server) which will gather BGP status for all MK routers. 
SNMP poller will poll this Server using extended oid, and server will execute the script as a response and reply 
reply to poller regarding BGP peers status. 

If everything is OK (ie All bgp peer is established), 1 is returned).

If there is a problem then info about the problematic peers is/are returned 


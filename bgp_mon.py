""" Retrieve down  BGP peers from Mikrotik Routers,
    print "1" if everything is ok,
    else print message about problematic BGP peers """

import sys
import os
from librouteros import  connect

DEBUG = False

def log(log_msg):
    """Print a message if DEBUG is True"""
    if DEBUG:
        print(log_msg)

def main():
    Dict1 = {}
    Dict2 = {}
    Flag = 1
    Count = 0
    

    #router loopback IP to be checked from a file
    #file should have only router loopback IP perline nothing else

    try:
        RouterID = [line.rstrip('\n') \
        for line in open('RouterID.txt')]
    except Exception:
        e = sys.exc_info()[0]
        log(e)
        sys.exit(1)

    ## Defining the API Connection
    for x in RouterID: 
        try:
            api = connect(username='admin', password='', host=x)
            ## Command run on each router
            bgp_peers = api(cmd='/routing/bgp/peer/print')
            for i in bgp_peers:
                if str(i['disabled']) == 'False':
                    Dict1.update({i['remote-address']: {'router_id': x, 'state': i['state']}} )
            api.close()

        except Exception:
            e = sys.exc_info()[0]
            log(e)
    
    
    #Finding Number of Down Peers.
    for Key, Value  in Dict1.items():
       if Dict1[Key]['state'] != "established":
          Dict2.update({Key: Value})
          Flag = 0
          Count += 1
    if Flag == 0: 
        print("%s peer_down"%(Count),end=': ')
        for Key, Value in Dict2.items():
            print("neighbor '%s' of router '%s' is down"%(Key,Value['router_id']),end=': ') 
    else:
        print(1) 
main()


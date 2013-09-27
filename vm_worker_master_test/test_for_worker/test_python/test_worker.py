#-*- coding: utf-8 -*-

import sys
import os
import time

#from gen.vm_worker.ttypes import AppInfo
from gen.worker.Worker import Client
from gen.worker.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.transport.TTransport import TTransportException

def test_vmworker(client):	
	#transport = TSocket.TSocket("localhost", 9090)
        #transport = TTransport.TBufferedTransport(transport)
        #protocol = TBinaryProtocol.TBinaryProtocol(transport)

	#client = Client(protocol)
	
	eax = 0
	#connect!
	#transport.open()
	print "set client ok"
	test_str = "hello txh"
	try:
		 client.test()
	except  TTransportException, tx:
        	print tx

	#close!
	#transport.close()

def sendheartbeat(client):
	heartbeat_app_info = HeartbeatAppInfo()
	heartbeat_app_info.app_id = 1
	heartbeat_app_info.state = AppState.APP_ONLINE
	try:
		client.sendheartbeat(heartbeat_app_info)
        except TTransportException, tx:
                print tx
	#print rtn
        #if(rtn == True):
        #        print "start_app ok"
        #else:
        #        print "start_app error"
	print "send heartbeat_app_info ok"
	
if __name__ == '__main__':
	timeout = 120000
	transport = TSocket.TSocket("localhost", 9090)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        client = Client(protocol)

	#connect!
	transport.open()

        #for function
        #test_vmworker(client)
	sendheartbeat(client)
	#count_num = 0
	#while True:
	    #if count_num == 10:
		#break
	    #count_num = count_num + 1
	#start_app(client)
	
	#time.sleep(50)
	#stop_app(client)
	#close!
        transport.close()


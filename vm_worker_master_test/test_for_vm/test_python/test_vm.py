#-*- coding: utf-8 -*-

import sys
import os
import time

#from gen.vm_worker.ttypes import AppInfo
from gen.vm_worker.VMWorker import Client
from gen.vm_worker.ttypes import VM_AppInfo

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
		eax = client.test(2, "ttt")
	except  TTransportException, tx:
        	print tx
	if(eax == 1):
		print "test ok"
	else:
		print "test error"

	#close!
	#transport.close()

def start_app(client):
	app_info = VM_AppInfo()
	app_info.id = 1
	app_info.name = "test"
	#app_info.source = "/root/test_txh/apps/test"
	#app_info.source = "/root/work/vm_worker_master_test/apps/test"
	app_info.install_dir = "/usr/bin"
	app_info.exe = "xeyes"
	app_info.argument = " " 
	app_info.run_type ="normal"
	app_info.interval = 10 
	rtn = False
        try:
                rtn = client.StartApp(app_info)
        except  TTransportException, tx:
                print tx
	#print rtn
        if(rtn == True):
                print "start_app ok"
        else:
                print "start_app error"

def install_app(client):
        app_info = VM_AppInfo()
        app_info.id = 1
        app_info.name = "test"
        app_info.source = "/root/test_txh/apps/test"
        #app_info.source = "/root/work/vm_worker_master_test/apps/test"
        app_info.install_dir = "/usr/bin"
        app_info.exe = "xeyes"
        app_info.argument = " "
        app_info.run_type ="normal"
        app_info.interval = 10
        rtn = False
        try:
                rtn = client.InstallApp(app_info)
        except  TTransportException, tx:
                print tx
        #print rtn
        if(rtn == True):
                print "install_app ok"
        else:
                print "install_app error"

def stop_app(client):
	exe = "test.sh"
	source = "/root/test_txh/apps/test_vm_worker_master_app/"
	id = 1
	rtn = False
	try:
                rtn = client.StopApp4Daemon(id)
        except  TTransportException, tx:
                print tx
	if(rtn == True):
		print "stop_app ok"
	else:
		print "stop_app error"

if __name__ == '__main__':
	timeout = 120000
	transport = TSocket.TSocket("192.168.10.163", 9991)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        client = Client(protocol)

	#connect!
	transport.open()

        #for function
        #test_vmworker(client)
	#count_num = 0
	#while True:
	    #if count_num == 10:
		#break
	    #count_num = count_num + 1
	install_app(client)
	#start_app(client)
	#stop_app(client)
	#time.sleep(10)
	#stop_app(client)
	#close!
        transport.close()


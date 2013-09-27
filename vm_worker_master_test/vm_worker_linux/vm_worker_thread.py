# -*- coding:utf-8 -*-
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.transport.TTransport import TTransportException

from rpc import Rpc
import time
import threading
from gen_worker.worker.Worker import Client
from gen_worker.worker.ttypes import *

def HeartbeatThread():
    while True:
	heartbeat_app_info = HeartbeatAppInfo()
        heartbeat_app_info.app_id = 1
        heartbeat_app_info.state = AppState.APP_ONLINE
	try :
		worker_client = Rpc(T = Client).GetProxy("192.168.120.249:9090")
                worker_client.sendheartbeat(heartbeat_app_info)
                #client.sendheartbeat(heartbeat_app_info)
        	print "yes_txh"
	except TTransportException, e:
		continue
	time.sleep(10)

def HeartbeatProcessor():
    #create thread
    heartbeat_thread = threading.Thread(target=HeartbeatThread)
    heartbeat_thread.start()
    count_num = 0
    #daemon thread
    while True:
	if not heartbeat_thread.is_alive():
		 heartbeat_thread = threading.Thread(target=HeartbeatThread)
	         heartbeat_thread.start()
	print count_num
	count_num = count_num + 1
	time.sleep(10)



#-*- coding:utf8 -*-
import sys
import os
#python不支持gen-py 中的特殊字符,所以将文件夹的名字改为gen
#主要是我想取文件名字为vm_worker.py，这个与自动生成的文件名冲突了

#这个是需要定义的一些类型
#from gen.master import Master
#from gen.master.ttypes import *

#文件名不能起跟vm_worker一样的
from gen.worker import Worker
from gen.worker.ttypes import *
#from gen.worker import Worker
#from gen.worker.ttypes import *

from thrift.transport.TTransport import TTransportException

from rpc import Rpc
#from vm_worker_config import VMWorkerConfigI
from worker_service import WorkerHandler
#from work_thread import HeartbeatProcessor
import threading

global state
if __name__ == '__main__':
    #初始化日志
    #logger = logging.getLogger('vm_worker')
    #hdlr = logging.FileHandler('vm_worker.log')
    #formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #hdlr.setFormatter(formatter)
    #logger.addHandler(hdlr)
    #logger.setLevel(logging.NOTSET)
    ##TODO
    #等待师兄给出IP解决方案#
    #初始化vm worker的配置
    #if not VMWorkerConfigI.Instance().Init('/media/CDROM/conf'):
    #    logger.error('read vm worker config error')
    #    exit

    #启动心跳线程
    #heartbeat_t = threading.Thread(target=HeartbeatProcessor)
    #heartbeat_t.setDaemon()
    #heartbeat_t.start()
    print "yes"
    #启动自身的rpc服务器
    Rpc(T = WorkerHandler, P = Worker.Processor).Listen(9090)

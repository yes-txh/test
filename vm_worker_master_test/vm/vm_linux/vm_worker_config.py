# -*- coding: utf-8 -*-

import ConfigParser
import os
from singleton import Singleton
import logging
from tool import Tool
import time

logger = logging.getLogger()
handler=logging.FileHandler("vm_worker.log")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.NOTSET)

class VMWorkerConfig:
    def __init__(self):
        self.attributes = {}
        
    def Init(self, config_file_name):
        while not os.path.exists(config_file_name):
            logger.error('can not find config file from cdrom')
            #光盘可能还没有识别
            #可能还未识别
            #可以尝试一定次数然后退出？
            time.sleep(2)
        
        cf = ConfigParser.ConfigParser()
        cf.read(config_file_name)
        value = cf.get('vm_worker', 'worker_endpoint')
        if(value == ''):
            logger.error('no worker_endpoint specified')
            return False
        self.attributes['worker_endpoint'] = value

        value = cf.get('vm_worker', 'port')
        if(value == ''):
            logger.error('no port specified')
            return False
        self.attributes['port'] = value

        value = cf.get('vm_worker', 'heartbeat_interval')
        if(value == ''):
            logger.error('no port specified')
            return False
        self.attributes['heartbeat_interval'] = value

        value = cf.get('vm_worker', 'ip')
        if(value == ''):
            logger.error('no ip specified')
            return False
        self.attributes['ip'] = value
        '''tool = Tool()
        if not tool.SetIP(value):
            logger.error('can not set ip')
            return False'''
        
        value = cf.get('vm_worker', 'job_id')
        if(value == ''):
            logger.error('no job_id specified')
            return False
        self.attributes['job_id'] = value

	value = cf.get('vm_worker', 'task_id')
        if(value == ''):
            logger.error('no task_id specified')
            return False
        self.attributes['task_id'] = value

	value = cf.get('vm_worker', 'interface')
        if(value == ''):
            logger.error('no interface specified')
            return False
        self.attributes['interface'] = value

        '''try:
            vfile = open('/root/vminfo.ini','w')
            vfile.write(value)
            vfile.close
        except OSError, e:
            logger.error(e)
            return False
        except IOError, e:
            logger.error(e)
            return False'''
        
        return True
        
    def Get(self, key):
        return self.attributes[key]

VMWorkerConfigI = Singleton(T=VMWorkerConfig)

if __name__ == '__main__':
    print "yes"
    #VMWorkerConfigI.Instance().Init('/meida/CDROM/conf')
    VMWorkerConfigI.Instance().Init('/root/work/vm_worker_master_test/vm_linux/conf')
    print 'vmworkerconfigI'
    print VMWorkerConfigI.Instance().Get('worker_endpoint')
    print VMWorkerConfigI.Instance().Get('ip')
    print VMWorkerConfigI.Instance().Get('port')
    print VMWorkerConfigI.Instance().Get('job_id')
    print VMWorkerConfigI.Instance().Get('heartbeat_interval')
    print VMWorkerConfigI.Instance().Get('task_id')
    print VMWorkerConfigI.Instance().Get('interface')

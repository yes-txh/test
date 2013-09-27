#-*- coding:utf8 -*-
import sys
import os
import threading
import subprocess
import time

sys.path.append('./gen')

# 导入thrift定义的模块
from gen.worker import Worker  # service
from gen.worker.ttypes import *  # struct

def IntervalRunWorker(source, exe, argument, interval):
	#周期启动应用程序
	count = 0
	while(True):
	    count = count + 1
	    print count #记录应用轮询次数
	    try:
                    state_file = open(source + '/daemon', 'r')
                    content = state_file.read()
		    state_file.close()
            	    if content == "stopped":
			print "stop ok"
                        return True
            except OSError, e:
                continue
            except IOError, e:
                continue 
  	    exe_path = source + "/" + exe
            cmd ='sh'+' '+ exe_path + ' ' + argument
            interval_p = subprocess.Popen(cmd, shell = True, cwd = source)
	    interval_p.wait()
	    		
	    time.sleep(interval)

def AppRunWorker(name, source, exe, argument, run_type, interval):
	if run_type == 'normal':
	    exe_path = source + "/" + exe
	    cmd ='sh'+' '+ exe_path + ' ' + argument
            p = subprocess.Popen(cmd, shell = True, cwd = source)
            p.wait()
	    return True

	elif run_type == 'daemon':
	    print "daemon"
	    '''exe_path = source + "/" + exe
            cmd ='sh'+' '+ exe_path + ' ' + argument
            p = subprocess.Popen(cmd, shell = True, cwd = source)'''    
	    try:
                #写个文件表示应用正在运行
                state_file = open(source + '/daemon','w')
                state_file.write('running')
                state_file.close()
	    except OSError, e:
                logger.error(e)
                return False
            except IOError, e:
                logger.error(e)
                return False
	    #启动周期运行应用线程
	    interval_run_worker = threading.Thread(target = IntervalRunWorker, args = (source, exe, argument,  interval))
            interval_run_worker.start()
 	    #守护周期运行线程
	    while(True):
		if not interval_run_worker.is_alive():
		    try:
                        state_file = open(source + '/daemon', 'r')
                        content = state_file.read()
			state_file.close()
                        if content == 'stopped':
                            return True
                    except OSError, e:
                        logger.error(e)
                        #return False
                        continue
                    except IOError, e:
                        logger.error(e)
                        #return False
                        continue
		    interval_run_worker = threading.Thread(target = IntervalRunWorker, args = (source, exe, argument, interval))
	            interval_run_worker.start()
		time.sleep(interval)
	    return True

	else:
	    print "unknown type" + run_type
	    return False

def AppStopWorker(exe, source):
	print exe
	try:
                #写个文件表示应用正在运行
                state_file = open(source + '/daemon','w')
                state_file.write('stopped')
                state_file.close()
        except OSError, e:
                logger.error(e)
                return False
        except IOError, e:
                logger.error(e)
                return False
	print"stop app ok"
	return True

class WorkerHandler:
    """
    负责处理rpc相关
    """
    def __init__(self):
        pass
    
    #def test( test_id, test_str):  TypeError: test() takes exactly 2 arguments (3 given)
    def test(self):
		print "hello world"
		return True

    def sendheartbeat(self, hb_vm_info):
		print hb_vm_info
		return True

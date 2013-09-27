#-*- coding: utf-8 -*-
import logging
import os
import sys
import time
import string
from singleton import Singleton
reload(sys)
sys.setdefaultencoding('utf-8')

logger = logging.getLogger('vm_worker')

class Tool:
     first=True
     prev_used = 0
     prev_total = 0

     #网关也要弄得传入
     def SetIP(self,ip):
	  #代码不好使,也可能ip确实被人用了，但是防火墙被关了，所以ping不通
          submask = '255.255.0.0'
          #联通
          if (ip.find('172.16.60') != -1):
               gateway  = '172.16.0.254'
          #电信
          elif (ip.find('172.17.60') != -1):
               gateway  = '172.17.0.254'
          #本机测试网络
          else:
               gateway  = '10.128.252.254'
          
          dns_server = '8.8.8.8'
	  setgw = 'route add default gw '+gateway
          setip='ifconfig eth0 '+ip+' netmask '+submask
	  setdns = 'nameserver '+dns_server
	  setroute ='route add -net 10.0.0.0 netmask 255.0.0.0 gw 192.168.122.1'
	  try :
		print "cmd :",setip,setdns
		#os.system('rm -rf /etc/udev/rules.d/70-persistent-net.rules')
		os.system('/etc/init.d/networking start')
		os.system('route del default dev eth0')
		os.system(setip+" ; "+setgw)
		os.system(setroute)
		
		try:
			##清空DNS文件，写入namesever
			f = open('/etc/resolv.conf','w')
		except IOError:
			f.close()
			print "/etc/resolv.conf can\'t open"
		f.write('#Generated by ZDPT\n'+setdns)
		f.close()
	  except(SystemExit):
		print "system exit" 
	  return True
# @return: cpu usage
     def GetCpuUsage(self):
    	#line_list
	try:
        	file_object = open('/proc/stat')
	except IOError:
		file_object.close()
		print "file open failed"
		return -1.0
	for line in file_object:
		if line.find("cpu ")!=-1:
			cpu_list=line[5:].split(" ")
			break
        cpu_user = float(cpu_list[0]);
        cpu_nice = float(cpu_list[1]);
        cpu_sys = float(cpu_list[2]);
        cpu_idle = float(cpu_list[3]);
        cpu_iowait = float(cpu_list[4]);
        cpu_hardirq =float( cpu_list[5]);
        cpu_softirq =float( cpu_list[6]);
        used = cpu_user + cpu_nice + cpu_sys +cpu_iowait + cpu_hardirq + cpu_softirq;
        total = used + cpu_idle;
        if Tool.first :
        	Tool.first = False;
        	Tool.prev_used = used;
        	Tool.prev_total = total;
        	file_object.close();
		return 0.0;
        if total == Tool.prev_total :
    		total =Tool.prev_total + 1;
    	cpu_usage =(used - Tool.prev_used)/(total - Tool.prev_total);
  	Tool.prev_used = used;
    	Tool.prev_total = total;
    	file_object.close()
	return cpu_usage;


     def GetMemoryUsage(self):
	  mem ={}
       	  try:
	  	f = open("/proc/meminfo")
          except IOError:
                f.close()
                print "/proc/meminfo file open failed"
                return -1.0
	  lines = f.readlines()
	  f.close()
	  for line in lines:
		if len(line)<2 :continue
	  	name = line.split(":")[0]
		var  = line.split(":")[1].split()[0]
		mem[name]=long(var)
	  mem['MemUsed']=mem['MemTotal']-mem['MemFree']-mem['Buffers']-mem['Cached']
	  #print "total:%ld,used:%ld" %(mem['MemUsed'],mem['MemTotal'])
	  return float(mem['MemUsed'])/float(mem['MemTotal'])

    
     def GetInNetUsage(self, interface):
          try:
                f = open("/proc/net/dev")
          except IOError:
                f.close()
                print "/proc/net/dev file open failed"
                return -1.0
          lines = f.readlines()
          f.close()
	  flag = False
	  for line in lines:
		if interface in line:
			word_list = line.split()
			flag = True
			bytes_in_str = word_list[1]
	  if flag == False:
		print "no found %s info" %(interface)
		return -1.0
	  bytes_in = string.atoi(bytes_in_str)
	  return bytes_in

     def GetOutNetUsage(self, interface):
          try:
                f = open("/proc/net/dev")
          except IOError:
                f.close()
                print "/proc/net/dev file open failed"
                return -1.0
          lines = f.readlines()
          f.close()
          flag = False
          for line in lines:
                if interface in line:
			word_list = line.split()
                        flag = True
                        bytes_out_str = word_list[9]
          if flag == False:
                print "no found %s info" %(interface)
                return -1.0
	  bytes_out = string.atoi(bytes_out_str)
          return bytes_out


#这个在多线程的时候会带来问题，不知道为什么不能共享context
#ToolI = Singleton(T=Tool)
if __name__ == '__main__':
     tool = Tool()
     '''tool.SetIP('172.16.60.23')
     while True:
	print "memusage:%2.2f%%" %(tool.GetMemoryUsage()*100)
        print "==========================="
	print "cpuusage:%2.2f%%" %(tool.GetCpuUsage()*100)
        time.sleep(2)'''
     bytes_in = 0
     bytes_out =0	
     bytes_in = tool.GetInNetUsage("eth0")
     bytes_out = tool.GetOutNetUsage("eth0")

     print bytes_in
     print bytes_out
#include<stdio.h>
#include<iostream>

#include "rpc.h"
#include "worker_service.h"

using namespace std;

int main(int argc, char ** argv)
{
  cout<<"test start at worker";
  Rpc<WorkerService, WorkerProcessor>::Listen(9090);
  return true;
/*      try {
        Proxy<VMWorkerClient> proxy = Rpc<VMWorkerClient, VMWorkerClient>::GetProxy();
        if(!proxy().test()) {
            cout<<"rpc error: can't test ";
            return false;
        }
    } catch (TException &tx) {
         cout<<"rpc error: test error " << tx.what();
         return false;
    }
    return true;

     //生成一个Socket连接到服务端
     TSocket* sc = new TSocket("localhost", 9090);
     shared_ptr<TTransport> socket(sc);
     //对Socket通道加入缓冲功能
     shared_ptr<TTransport> transport(new TBufferedTransport(socket));
     //生成相应的二进制协议，这个要和服务端一致
     shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));
    //生成客户端服务对象
     VMWorkerClient client;

     try{
	    transport->open();
	    client.test();
	    cout<<"yes world";
	}
     catch (TException &tx) {
         cout<<"rpc error: test error " << tx.what();
         return false;
     return true;
}
*/

}

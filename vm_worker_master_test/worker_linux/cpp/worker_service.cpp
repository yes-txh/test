#include <iostream>

#include "vm_worker/gen-cpp/VMWorker.h"
#include "worker/gen-cpp/Worker.h"
#include "rpc.h"

using namespace std;

WorkerService::test()
{
   try {
        Proxy<VMWorkerClient> proxy = Rpc<VMWorkerClient, VMWorkerClient>::GetProxy();
        if(!proxy().test()){
            LOG(ERROR) << "rpc error: test";
            return false;
        }
    } catch (TException &tx) {
         LOG(ERROR) << "rpc error: test error " << tx.what();
         return false;
    }
}

WorkerService::test_worker()
{
   cout<<"test for worker ok !";
   return true;
}
~    
WorkerService::start_app()
{
    try {
        Proxy<VMWorkerClient> proxy = Rpc<VMWorkerClient, VMWorkerClient>::GetProxy();
        if(!proxy().start_app()){
            LOG(ERROR) << "rpc error: start_app";
            return false;
        }
    } catch (TException &tx) {
         LOG(ERROR) << "rpc error: start_app error " << tx.what();
         return false;
    }

}
~    
WorkerService::query_app()
{
    try {
        Proxy<VMWorkerClient> proxy = Rpc<VMWorkerClient, VMWorkerClient>::GetProxy();
        if(!proxy().query_app()){
            LOG(ERROR) << "rpc error: query_app";
            return false;
        }
    } catch (TException &tx) {
         LOG(ERROR) << "rpc error: query_app error " << tx.what();
         return false;
    }

}
~    

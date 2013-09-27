#include <protocol/TBinaryProtocol.h>
#include <transport/TTransport.h>
#include <transport/TSocket.h>
#include <transport/TTransportException.h>

#include <string>
#include <iostream.h>

#include "gen/VMWorker.h"

using std::string;

using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;
using namespace apache::thrift::TException

using boost::shared_ptr;
using std::cout;

int main(int argc, char** argv)
{
    TSocket* sc = new TSocket("localhost", 9090);
    shared_ptr<TTransport> socket(sc);
    shared_ptr<TTransport> transport(new TBufferedTransport(socket));
    shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));

    VMWorkerClient client(protocol);
    string test_str = "yes";    
    try{ 
            transport->open();
            client.test(1,test_str); 
            cout<<"yes world";
       }
    catch (TException &tx) {
         cout<<"rpc error: test error " << tx.what();
         return false;
	}
    transport->close();
    return true;    

}

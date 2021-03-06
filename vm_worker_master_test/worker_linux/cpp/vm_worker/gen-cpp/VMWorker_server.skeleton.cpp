// This autogenerated skeleton file illustrates how to build a server.
// You should copy it to another filename to avoid overwriting it.

#include "VMWorker.h"
#include <protocol/TBinaryProtocol.h>
#include <server/TSimpleServer.h>
#include <transport/TServerSocket.h>
#include <transport/TBufferTransports.h>

using namespace ::apache::thrift;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace ::apache::thrift::server;

using boost::shared_ptr;

using namespace  ;

class VMWorkerHandler : virtual public VMWorkerIf {
 public:
  VMWorkerHandler() {
    // Your initialization goes here
  }

  bool test() {
    // Your implementation goes here
    printf("test\n");
  }

  bool start_app() {
    // Your implementation goes here
    printf("start_app\n");
  }

  bool query_app() {
    // Your implementation goes here
    printf("query_app\n");
  }

};

int main(int argc, char **argv) {
  int port = 9090;
  shared_ptr<VMWorkerHandler> handler(new VMWorkerHandler());
  shared_ptr<TProcessor> processor(new VMWorkerProcessor(handler));
  shared_ptr<TServerTransport> serverTransport(new TServerSocket(port));
  shared_ptr<TTransportFactory> transportFactory(new TBufferedTransportFactory());
  shared_ptr<TProtocolFactory> protocolFactory(new TBinaryProtocolFactory());

  TSimpleServer server(processor, serverTransport, transportFactory, protocolFactory);
  server.serve();
  return 0;
}


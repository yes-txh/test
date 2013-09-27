#!/bin/bash
thrift --gen py -r ../proxy/vm_worker/vm_worker.thrift
thrift --gen py -r ../proxy/worker/worker.thrift
thrift --gen py -r ../proxy/client/client.thrift
thrift --gen py -r ../proxy/master/master.thrift
mv gen-py gen


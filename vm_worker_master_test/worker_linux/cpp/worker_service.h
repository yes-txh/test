#ifndef LYNN_SRC_WORKER_CELLET_SERVICE_H_
#define LYNN_SRC_WORKER_CELLET_SERVICE_H_

#include <string>
#include <vector>
#include "worker/gen-cpp/Worker.h"
#include "vm_worker/gen-cpp/VMWorker.h"

using std::string;
using std::vector;

class WorkerService : public WorkerIf {
public:
      bool test();
      bool test_worker();
      bool start_app();
      bool query_app();
};

#endif

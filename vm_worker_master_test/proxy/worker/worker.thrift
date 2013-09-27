enum AppState {
    APP_NOTFOUND,
    APP_ONLINE,
    APP_FAILED,
    APP_FINISHED,
}

enum VMState {
    VM_NOTFOUND,
    VM_OFFLINE,
    VM_ONLINE,
    VM_SERVICE_ONLINE,
}

struct VM_HbAppInfo{
    1: i32 id,
    2: string name,
    3: AppState state,
    4: i32 error_id,
    5: bool app_install,
}

struct VM_HbVMInfo{
    1: i32 job_id,
    2: i32 task_id,
    3: double cpu_usage,
    4: double memory_usage,
    5: i32 bytes_in,
    6: i32 bytes_out,
    7: VMState state,
    8: bool app_running,
    9: VM_HbAppInfo hb_app_info
}

service Worker {
    bool test(),
    bool sendheartbeat(1:VM_HbVMInfo hb_vm_info),
    bool AppInstalled(1:i32 job_id, 2:i32 task_id, 3:i32 app_id)
}

struct VM_AppInfo {
    1: i32 id,
    2: string name,
    3: string source,
    4: string install_dir,
    5: string exe,
    6: string argument,
    7: string out_dir,
    8: string app_out_dir,
    9: string run_type, 
    10: i32 interval,
}

service VMWorker {
    bool test(1:i32 id, 2:string str),
    bool InstallApp(1:VM_AppInfo app_info),
    bool StartApp(1:VM_AppInfo app_info),
    bool StopApp(1:i32 id, 2:string stop),
    bool StopApp4Daemon(1:i32 id),
}

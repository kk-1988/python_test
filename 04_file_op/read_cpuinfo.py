with open("/proc/cpuinfo",'r') as fobj:
    for line in fobj:
        print(line,end ='')

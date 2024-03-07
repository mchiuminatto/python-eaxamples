from multiprocessing import Process
import os
import time

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def func(name):
    print(name)
    while True:
        info('function f')
        print('hello', name)
        time.sleep(5)

if __name__ == '__main__':


    # starting up proceses

    # read scenaro list
    info('main process')
    
    proc_list =[]


    proc_list.append(Process(target=func, args=('marcello',)))
    proc_list[0].start()
    proc_list.append(Process(target=func, args=('sofia',)))
    proc_list[1].start()
    while True:
        for v in proc_list:
            print("At parent process: " + str(v.pid))

#!/bin/python3

import sys
import socket
import threading
from datetime import datetime 
import concurrent.futures

def scan(target, port):
    socket.setdefaulttimeout(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"port {port} is open")
    s.close()

'''
if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
        print("-"*30)
        print("Scanning target: "+target)
        print("Time started: "+str(datetime.now()))
        print("-"*30)
        threads = []
        for port in range(1, 81):
            x = threading.Thread(target=scan, args=[target,port])
            threads.append(x)
            x.start()
        for thread in threads:
            thread.join()
        print('done ??')
    except:
        print("invalid input")
else:
    print("Syntax error: invalid number of arguments")'''


 
if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
        print("-"*30)
        print("Scanning target: "+target)
        print("Time started: "+str(datetime.now()))
        print("-"*30)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for port in range(1, 81):
                executor.submit(scan, target, port)
 
        print('done ??')
    except:
        print("invalid input")
else:
    print("Syntax error: invalid number of arguments") 
 

 
 

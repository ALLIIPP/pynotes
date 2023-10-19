#!/usr/bin/python3




#multiprocessing
#---------------------------------------------------------------
'''
multiprocessing - running tasks in parallel on different cpu cores, bypasses GIL
                - used for threading
'''

from multiprocessing import Process, cpu_count
import time

def counter(num):
    counter = 0
    while counter <num:
        counter +=1


def main():
    start = time.perf_counter()
    a = Process(target=counter, args=(250_000_000,))            # create a Process object // args must end with ',' to differentiate from expression
    b = Process(target=counter, args=(250_000_000,))
    c = Process(target=counter, args=(250_000_000,))
    d = Process(target=counter, args=(250_000_000,))

    '''
    a.start()                                                   # begins the process 
    b.start()
    c.start()
    d.start()

    a.join()                                                    # force main thread to wait until process finishes
    b.join()
    c.join()
    d.join()
    '''
    print(cpu_count())
    print('finished in {} seconds'.format(time.perf_counter() - start))

if __name__ == '__main__':
    main()                                                      #in windows? seperate threads will recreate entire module so youll get an infinite loop
                                                                # so check '__main__' so that its only called once

#---------------------------------------------------------------

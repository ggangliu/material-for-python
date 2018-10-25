# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tqdm import tqdm, trange
from time import sleep
import threading

lock = threading.RLock()
con = threading.Condition()
event = threading.Event()
    
def example3():
    event.wait()
    pbar = tqdm(["a", "b", "c", "d"], desc='customer')
    for char in pbar:
        sleep(1)

def example2():
    text = ""
    for char in tqdm(["a", "b", "c", "d"], desc='generator'):
        sleep(1)
        text = text + char
    #Notify example3 to run    
    event.set()   
    
def example1():
    for i in trange(100, desc='example1'):
        sleep(0.1)
    


if __name__ == '__main__':

    t1 = threading.Thread(target=example1) 
    t2 = threading.Thread(target=example2) 
    t1.setDaemon(False)
    t2.setDaemon(False)
    t1.start()
    t2.start()
    
    ####################
    t3 = threading.Thread(target=example3)
    t3.setDaemon(False)
    t3.start()
    
    print("main end")

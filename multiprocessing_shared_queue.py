from itertools import cycle
from multiprocessing import Process, Lock, Queue

def add_int_to_queue(q):
    for i in range(100):
        q.put(i)
    q.put(None) # Introduce a poison pill to break q.get

def add_str_to_queue(q):
    count = 0
    for i in cycle(['a','b','c']):
        q.put(i)
        count+=1
        if count==15:
            break
    q.put(None) # Introduce a poison pill to break q.get


if __name__ =="__main__":
    q = Queue()
    p1 = Process(target=add_str_to_queue,args=(q,))
    p2 = Process(target=add_int_to_queue,args=(q,))

    p1.start()
    p2.start()
    stop_counter=0
    while True:
        item=q.get()
        if item is None: # Checking for poison pill
            stop_counter+=1
            if stop_counter == 2:
                break
        else:
            print(item)

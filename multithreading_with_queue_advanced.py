from threading import Thread, Lock, current_thread
from queue import Queue

counter = 0
def read_from_queue_increament_operator(lock:Lock,q:Queue):
    global counter
    while True:
        value = q.get()
        with lock:
            print(f"Received message-{counter} from queue on thread:{current_thread().name} DATA:{value}")
            counter+=1
        q.task_done()

if __name__=="__main__":
    q = Queue()
    lock = Lock()
    thread1=Thread(target=read_from_queue_increament_operator,args=(lock,q))
    thread2=Thread(target=read_from_queue_increament_operator,args=(lock,q))
    thread1.daemon = True
    thread2.daemon = True
    thread1.start()
    thread2.start()

    for i in range(1000):
        q.put(i)

    q.join()
    print("THREAD PROCESSING COMPLETED")








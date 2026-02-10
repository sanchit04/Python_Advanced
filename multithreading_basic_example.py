from threading import Thread,Lock

def square_number(lock):
    lock.acquire()
    for i in range(1000):
        print(i*i)
    lock.release()


if __name__=="__main__":
    thread_list = []
    num_threads=10
    lock=Lock()

    for _ in range(num_threads):
        t = Thread(target=square_number,args=(lock,))
        thread_list.append(t)

    # START THE THREAD:
    for t in thread_list:
        t.start()

    # Blocks main thread until all threads complete the processing
    for t in thread_list:
        t.join()

    print("END MAIN")
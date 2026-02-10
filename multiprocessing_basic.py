from multiprocessing import Process,Lock
import os

def square_numbers(lock):
    with lock:
        for i in range(1000):
            print(i*i)

if __name__ == "__main__":
    num_count = os.cpu_count()
    lock=Lock()
    process_list=[]

    for _ in range(num_count):
        p=Process(target=square_numbers,args=(lock,))
        process_list.append(p)

    for p in process_list:
        p.start()

    for p in process_list:
        p.join()

    print("END MAIN")
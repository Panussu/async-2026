from time import sleep, ctime, time, process_time
import multiprocessing
import threading
import os
import psutil

def make_coffee(customer_name, result_queue):

    pid = os.getpid()
    tid = threading.current_thread().native_id

    start_cpu = process_time()

    print(f"{ctime()} | [PID:{pid}] [TID:{tid}] Serving {customer_name}")

    sum(i * i for i in range(1000000))
    sleep(5)

    cpu_time = process_time() - start_cpu

    process = psutil.Process(pid)
    ram = process.memory_info().rss / (1024 * 1024)

    result_queue.put((ram, cpu_time))

def main():

    queue = ['A', 'B', 'C']

    start_time = time()
    main_cpu = process_time()

    result_queue = multiprocessing.Queue()
    processes = []

    for customer in queue:
        p = multiprocessing.Process(
            target=make_coffee,
            args=(customer, result_queue)
        )
        processes.append(p)
        p.start()

    child_ram = []
    child_cpu = []

    for _ in queue:
        ram, cpu = result_queue.get()
        child_ram.append(ram)
        child_cpu.append(cpu)

    for p in processes:
        p.join()

    wall_time = time() - start_time

    main_process = psutil.Process(os.getpid())
    main_ram = main_process.memory_info().rss / (1024 * 1024)

    total_ram = main_ram + sum(child_ram)
    total_cpu = (process_time() - main_cpu) + sum(child_cpu)

    print("\n[Multi-process]")
    print(f"Wall Time : {wall_time:.2f} sec")
    print(f"CPU Time  : {total_cpu:.4f} sec")
    print(f"RAM Usage : {total_ram:.2f} MB")

if __name__ == "__main__":
    main()
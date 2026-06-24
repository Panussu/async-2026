from time import sleep, ctime, time, process_time
import os
import threading
import psutil

def make_coffee(customer_name):
    pid = os.getpid()
    tid = threading.current_thread().native_id

    print(f"{ctime()} | [PID:{pid}] [TID:{tid}] Serving {customer_name}")

    sum(i * i for i in range(1000000))
    sleep(5)

    print(f"{ctime()} | Customer {customer_name} served")

def main():
    queue = ['A', 'B', 'C']

    start_time = time()
    start_cpu = process_time()

    for customer in queue:
        make_coffee(customer)

    wall_time = time() - start_time
    cpu_time = process_time() - start_cpu

    process = psutil.Process(os.getpid())
    ram = process.memory_info().rss / (1024 * 1024)

    print("\n[Synchronous]")
    print(f"Wall Time : {wall_time:.2f} sec")
    print(f"CPU Time  : {cpu_time:.4f} sec")
    print(f"RAM Usage : {ram:.2f} MB")

if __name__ == "__main__":
    main()
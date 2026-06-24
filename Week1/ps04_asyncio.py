from time import ctime, time, process_time
import asyncio
import os
import threading
import psutil

async def make_coffee(customer_name):

    pid = os.getpid()
    tid = threading.current_thread().native_id

    print(f"{ctime()} | [PID:{pid}] [TID:{tid}] Serving {customer_name}")

    sum(i * i for i in range(1000000))

    await asyncio.sleep(5)

    print(f"{ctime()} | Customer {customer_name} served")

async def main():

    queue = ['A', 'B', 'C']

    start_time = time()
    start_cpu = process_time()

    tasks = []

    for customer in queue:
        tasks.append(
            asyncio.create_task(make_coffee(customer))
        )

    await asyncio.gather(*tasks)

    wall_time = time() - start_time
    cpu_time = process_time() - start_cpu

    process = psutil.Process(os.getpid())
    ram = process.memory_info().rss / (1024 * 1024)

    print("\n[Asyncio]")
    print(f"Wall Time : {wall_time:.2f} sec")
    print(f"CPU Time  : {cpu_time:.4f} sec")
    print(f"RAM Usage : {ram:.2f} MB")

if __name__ == "__main__":
    asyncio.run(main())
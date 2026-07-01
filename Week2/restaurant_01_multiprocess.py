import multiprocessing
from time import sleep, ctime, time

def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

def customer_private_workflow(customer):

    print(f"{ctime()} [Process-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()} [Process-{customer}] Taking Order ...Done!")
    
    print(f"{ctime()} [Process-{customer}] Cooking Spaghetti ...")
    sleep(1)
    print(f"{ctime()} [Process-{customer}] Cooking Spaghetti ...Done!")
    
    print(f"{ctime()} [Process-{customer}] Manage Bar for Drink ...")
    sleep(1)
    print(f"{ctime()} [Process-{customer}] Manage Bar for Drink ...Done!")
    print(f"{ctime()} [Process-{customer}] All served in this branch!\n")

if __name__ == "__main__":
    customers = ['A', 'B', 'C']
    start_time = time()
    
    for customer in customers:
        greet_diners(customer)
        
    print(f"\n{ctime()} --- All customers greeted. FORKING into independent Processes (Branches) ---\n")
    
    processes = []
    for customer in customers:

        p = multiprocessing.Process(target=customer_private_workflow, args=(customer,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
        
    duration = time() - start_time
    print(f"{ctime()} Finished Entire Restaurant Operation in {duration:.2f} seconds.")
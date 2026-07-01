from time import sleep, ctime, time
import threading


def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")


def customer_private_workflow(customer):

    print(f"{ctime()} [Thread-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Taking Order ...Done!")


    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti ...Done!")


    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drinks ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drinks ...Done!")

    print(f"{ctime()} [Thread-{customer}] All served!\n")


if __name__ == "__main__":
    customers = ['A', 'B', 'C']
    start_time = time()

    for customer in customers:
        greet_diners(customer)

    print(f"\n{ctime()} ---- All customers greeted. Splitting into individual threads ----\n")

    customer_threads = []

    for customer in customers:

        t = threading.Thread(
            target=customer_private_workflow,
            args=(customer,)
        )

        customer_threads.append(t)
        t.start()

    for t in customer_threads:
        t.join()

    duration = time() - start_time

    print(f"\n{ctime()} Finished Entire Restaurant Operation in {duration:.2f} seconds.")
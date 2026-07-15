import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen


async def main():
    MY_STUDENT_ID = "6710301011"

    print(
        f"{ctime()} | --- [Task 2] "
        "Practice using gather to wait for all group orders ---"
    )

    start_time = time()

    # Create multiple orders concurrently
    task1 = send_order_to_kitchen(
        MY_STUDENT_ID,
        "hainanese_chicken",
        "Chicken Rice"
    )

    task2 = send_order_to_kitchen(
        MY_STUDENT_ID,
        "noodle",
        "Wonton Noodles"
    )

    task3 = send_order_to_kitchen(
        MY_STUDENT_ID,
        "steak",
        "Sizzling Steak"
    )

    # Wait for all dishes using asyncio.gather()
    results = await asyncio.gather(task1, task2, task3)

    # Print the results
    for result in results:
        shop = result.get("shop", "unknown")
        menu = result.get("menu", "unknown")

        print(
            f"{ctime()} | [Pickup] Shop: {shop} | "
            f"Menu: {menu} is ready!"
        )

    elapsed = time() - start_time

    print(
        f"{ctime()} | Total time: {elapsed:.2f} seconds "
        "(Equals to the slowest dish)."
    )


if __name__ == "__main__":
    asyncio.run(main())
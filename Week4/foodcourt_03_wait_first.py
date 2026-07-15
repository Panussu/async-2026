# foodcourt_03_wait_first.py
import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen


async def main():
    MY_STUDENT_ID = "6710301011"

    print(
        f"{ctime()} | --- [Task 3] "
        "Practice using wait (FIRST_COMPLETED) ---"
    )

    start_time = time()

    # Create three separate order tasks
    tasks = [
        asyncio.create_task(
            send_order_to_kitchen(
                MY_STUDENT_ID,
                "hainanese_chicken",
                "Chicken Rice Thigh"
            )
        ),
        asyncio.create_task(
            send_order_to_kitchen(
                MY_STUDENT_ID,
                "noodle",
                "Wonton Noodles"
            )
        ),
        asyncio.create_task(
            send_order_to_kitchen(
                MY_STUDENT_ID,
                "steak",
                "Sizzling Steak"
            )
        )
    ]

    # Wait until the first order is completed
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    # Get and display the fastest completed order
    winner_task = next(iter(done))
    winner = winner_task.result()

    shop = winner.get("shop", "unknown")
    menu = winner.get("menu", "unknown")

    print(
        f"{ctime()} | Winner served dish: "
        f"Shop: {shop} | Menu: {menu}"
    )

    # Cancel all remaining pending orders
    print(
        f"{ctime()} | Cleaning up: "
        f"Canceling {len(pending)} remaining pending orders..."
    )

    for task in pending:
        task.cancel()

    # Wait for the canceled tasks to finish cleaning up
    await asyncio.gather(*pending, return_exceptions=True)

    elapsed = time() - start_time

    print(
        f"{ctime()} | Total waiting time for the first dish: "
        f"{elapsed:.2f} seconds."
    )


if __name__ == "__main__":
    asyncio.run(main())
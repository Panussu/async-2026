# foodcourt_05_mix_concepts.py
import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen


async def main():
    MY_STUDENT_ID = "6710301011"
    TIMEOUT_LIMIT = 1.0

    print(
        f"{ctime()} | --- [Task 5] "
        "Advanced Practice: Mixing concepts together ---"
    )

    start_time = time()

    # Normal noodle order
    noodle_task = asyncio.create_task(
        send_order_to_kitchen(
            MY_STUDENT_ID,
            "noodle",
            "Wonton Noodles"
        )
    )

    # Chicken rice order with a strict 1-second timeout
    chicken_task = asyncio.create_task(
        asyncio.wait_for(
            send_order_to_kitchen(
                MY_STUDENT_ID,
                "hainanese_chicken",
                "Chicken Rice"
            ),
            timeout=TIMEOUT_LIMIT
        )
    )

    try:
        # Wait for both tasks to finish
        results = await asyncio.gather(
            noodle_task,
            chicken_task
        )

        print(
            f"{ctime()} | Success: All food served on time! "
            f"Received {len(results)} dishes."
        )

    except TimeoutError:
        print(
            f"{ctime()} | Timeout: Chicken rice took longer than "
            f"{TIMEOUT_LIMIT:.1f} second."
        )

        # Cancel unfinished tasks
        for task in (noodle_task, chicken_task):
            if not task.done():
                task.cancel()

        await asyncio.gather(
            noodle_task,
            chicken_task,
            return_exceptions=True
        )

    except Exception as error:
        print(
            f"{ctime()} | Unexpected error: "
            f"{type(error).__name__}: {error}"
        )

    elapsed = time() - start_time

    print(
        f"{ctime()} | Total elapsed time: "
        f"{elapsed:.2f} seconds."
    )


if __name__ == "__main__":
    asyncio.run(main())
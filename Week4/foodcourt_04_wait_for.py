# foodcourt_04_wait_for.py
import asyncio
from time import ctime
from food_utils import send_order_to_kitchen


async def main():
    MY_STUDENT_ID = "6710301011"
    TIMEOUT_LIMIT = 2.0

    print(
        f"{ctime()} | --- [Task 4] "
        "Practice using wait_for to handle timeouts ---"
    )

    print(
        f"{ctime()} | [System] Order sent. "
        f"Monitoring {TIMEOUT_LIMIT:.1f}s timeout limit..."
    )

    try:
        # Wait for the steak order, but only for 2 seconds
        result = await asyncio.wait_for(
            send_order_to_kitchen(
                MY_STUDENT_ID,
                "steak",
                "Sizzling Steak"
            ),
            timeout=TIMEOUT_LIMIT
        )

        shop = result.get("shop", "unknown")
        menu = result.get("menu", "unknown")

        print(
            f"{ctime()} | [Pickup] Shop: {shop} | "
            f"Menu: {menu} is ready!"
        )

    except asyncio.TimeoutError:
        print(
            f"{ctime()} | Timeout occurred: Steak took too long! "
            "Leaving the food court now."
        )


if __name__ == "__main__":
    asyncio.run(main())
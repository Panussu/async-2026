import asyncio


# Delivery System: นักศึกษาต้องเขียน try...except CancelledError ได้ถูกต้อง
# และใช้ .get_name(), .cancel(), และ .cancelled() ได้

async def delivery_task(package_id, duration):
    try:
        print(f"Start delivering package {package_id}...")
        await asyncio.sleep(duration)
        print(f"Package {package_id} delivered successfully.")
        return f"Package {package_id} Delivered!"

    except asyncio.CancelledError:
        print("Delivery Canceled! Returning package to warehouse.")
        raise


async def main():
    task = asyncio.create_task(
        delivery_task("P001", 5.0),
        name="Express-Courier"
    )

    await asyncio.sleep(2)

    print(f"Task name: {task.get_name()}")
    print(f"Task done?: {task.done()}")

    if not task.done():
        print("Delivery is taking too long.")
        print("Canceling delivery task...")
        task.cancel()

    try:
        result = await task
        print(result)

    except asyncio.CancelledError:
        print(f"Task cancelled?: {task.cancelled()}")


asyncio.run(main())
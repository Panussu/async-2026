import asyncio
from time import ctime

async def delivery_task(package_id, duration):
    try:
        print(f"{ctime()}Courier Start delivering {package_id}...")
        await asyncio.sleep(duration)
        return f"Package {package_id} Delivered!"
    except asyncio.CancelledError:
        print(f"{ctime()}Delivery Canceled! Returning package to warehouse.")
        raise

async def main():
    task = asyncio.create_task(delivery_task("P001", 5.0))
    task.set_name("Express-Courier")
    
    print(f"{ctime()}Package is in transit...")
    await asyncio.sleep(2.0)

    print(f"{ctime()}Checking task status:")
    print(f"{ctime()}Is task done? : {task.done()}")
    print(f"{ctime()}Task Name: {task.get_name()}")
    
    if not task.done():
        print(f"{ctime()}Delivery is taking too long! Canceling task...")
        task.cancel()
        
        try:
            await task
        except asyncio.CancelledError:
            pass
        

        print(f"{ctime()}Is task cancelled? : {task.cancelled()}")

if __name__ == "__main__":
    asyncio.run(main())
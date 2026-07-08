import asyncio
from time import ctime


# นักเรียนต้องเลือกใช้ asyncio.wait() พร้อมออปชั่น return_when=asyncio.FIRST_COMPLETED เท่านั้น
# หากใครใช้ gather หรือ wait_for จะไม่ตรงสเปคเงื่อนไขการแข่งขันข้อมูล

async def fetch_stock_price(server_name, delay):
    await asyncio.sleep(delay)
    return f"[{server_name}] Price: 150 USD"


async def main():
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha", 3.0)),
        asyncio.create_task(fetch_stock_price("Beta", 0.8)),
        asyncio.create_task(fetch_stock_price("Gamma", 1.5)),
    }

    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    for task in done:
        print(f"{ctime()} Winner Result: {task.result()}")

    print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")

    for task in pending:
        task.cancel()

    await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())
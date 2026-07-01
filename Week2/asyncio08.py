# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.
import asyncio
from time import ctime

async def kitchen_crew():
    print(f"{ctime()} -> [Chef] puts noodle in boiling water...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> [Chef] strains the noodle!")

async def bar_crew():
    print(f"{ctime()} -> [Bar] starts grinding coffee bean...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> [Bar] pours espresso shot!")

async def main():
    taskkitchen = asyncio.create_task(kitchen_crew())
    taskbar = asyncio.create_task(bar_crew())

    await taskkitchen
    await taskbar

if __name__ == "__main__":
    asyncio.run(main())
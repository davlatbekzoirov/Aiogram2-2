import asyncio
import datetime as dt
from scheduler.asyncio import Scheduler
async def foo(args):
    print("foo")
    await asyncio.sleep(1)

async def main():
    schedule = Scheduler()
    schedule.once(dt.timedelta(seconds=5),foo("args"))
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())
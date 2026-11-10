import asyncio
import time

async def fetch_quote(pair):
    await asyncio.sleep(0.5)  # stands for a netowork call
    return f"{pair} 1.0850"

async def one_by_one():
    for pair in ("EURUSD", "GBPUSD", "USDJPY"):
        await fetch_quote(pair)  #  wait for each before starting the next

async def all_at_once():
    async with asyncio.TaskGroup() as tg:  # start all three, then wait for all
        for pair in ("EURUSD", "GBPUSD", "USDJPY"):
            tg.create_task(fetch_quote(pair))

async def main():
    for fn in (one_by_one, all_at_once):
        t0 = time.perf_counter()
        await fn()
        print(f"{fn.__name__:<12} {time.perf_counter() - t0: 0.2f}s")

asyncio.run(main())
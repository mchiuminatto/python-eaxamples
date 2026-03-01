#!/usr/bin/env python3
# gather_records.py

import asyncio
import time


async def process_record(record: dict) -> str:
    """Simulates an async I/O operation per record (e.g. API call, DB query)."""
    await asyncio.sleep(3)  # simulate I/O latency
    value = f"Processed record id={record['id']}" 
    print(value)
    return value


async def main(records: list[dict]):
    # Build the list of coroutines dynamically from any iterable
    coroutines = [process_record(record) for record in records]

    # Unpack the list into gather — works for 10, 1500, 2000, or any size
    results = await asyncio.gather(*coroutines)

    return results


if __name__ == "__main__":
    # Simulate loading records from a file (could be 1500 or 2000 depending on run)
    records = [{"id": i, "value": f"data_{i}"} for i in range(2000)]

    s = time.perf_counter()
    results = asyncio.run(main(records))
    elapsed = time.perf_counter() - s

    print(f"Processed {len(results)} records in {elapsed:0.2f} seconds.")
    print(f"First result : {results[0]}")
    print(f"Last result  : {results[-1]}")

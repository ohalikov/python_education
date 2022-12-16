import asyncio
import time


async def say_message(delay, message):
    await asyncio.sleep(delay)
    print(message)


async def main():
    print(time.strftime('%X'))
    await say_message(1, "Hello")
    await say_message(3, "World")
    print(time.strftime('%X'))


async def main_modified():
    task1 = asyncio.create_task(
        say_message(1, 'hello_modified'))

    task2 = asyncio.create_task(
        say_message(4, 'world'))

    print(f"\n\nstarted at time: {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

# 3.11 PYTHON
async def main_modern_modified():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_message(1, 'hello'))

        task2 = tg.create_task(
            say_message(2, 'world'))

        print(f"\n\nstarted at {time.strftime('%X')}")

    # The wait is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
for i in range(0, 5):
    print("Bla Bla")


asyncio.run(main_modified())


asyncio.run(main_modern_modified())

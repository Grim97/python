import asyncio
import time

async def testing():
    print("Enada idhu")
    await asyncio.sleep(5)
    time.sleep(10)
    print("podhum")

async def testing2():
    print("In secod coroutine function")

async def main():
    print("Naveen Kumar")
    task1 = asyncio.create_task(testing())
    task2 = asyncio.create_task(testing2())
    result = await task1
    result2 = await task2
    print("coroutine end")
    print(result, result2)


asyncio.run(main())


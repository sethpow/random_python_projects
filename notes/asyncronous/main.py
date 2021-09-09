import asyncio


def greet():
    print('Hello Seth')


async def bye():
    await asyncio.sleep(2)
    print('Goodbye Seth')


async def main():
    greet()
    await bye()


asyncio.run(main())
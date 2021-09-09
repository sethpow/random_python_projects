import asyncio


'''
    coroutine: wrapped version of a fn that allows it to run asyncronously
        - returned from an async fn
        - anything with async before it
        await executes the coroutine

    need to define an event loop to run async code
        - design pattern that waits for and dispatches events/msg's
'''


async def main():
    print('Hello Seth')
    # await foo('Goodbye Seth')
    # task - runs code w/o waiting for await to complete
        # start executing ASAP, but allow other code to run in meantime
    task = asyncio.create_task(foo('Goodbye Seth'))
    # await task # now we wait for task to finish to run following lines

    await asyncio.sleep(.5)

    print('Working...')


async def foo(text):
    print(text)
    await asyncio.sleep(10)


# main() is the coroutine in this event loop
asyncio.run(main())
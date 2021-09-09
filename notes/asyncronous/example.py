import asyncio

# if you want a value from an asyncronous fn, you must await it
    # if you create a task, you can await the task to finish
    # simply awaiting task1 w/o create_task will wait for task1 to completely finish before running task2


async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(.25)

async def main():
    # future - placeholder for obj that will exist in the future
        # JS promise
        # value that will be returned in the future
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    
    # wait for task1 to finish running to move on
        # but since it is delayed 2 seconds, task 2 can run in mean time
        # it delays for .25 seconds every 0-9, and task1 can finish in that first .25 break in the 2s sleep
    value = await task1 # ensures task1 is finished and assign the returned value to 'value'
    print(value)

    await task2

asyncio.run(main())
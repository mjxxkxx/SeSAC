import time

def task(task_num, duration):
    print(f"started {task_num}")
    time.sleep(duration)
    print(f"ended {task_num}")

def main():
    begin = time.time()
    task1 = task(1, 3)
    task2 = task(2, 2)
    task3 = task(3, 1)

    end = time.time()

    print(f"Task time is {end - begin}")

main()


# async
import asyncio
import time
async def async_task(task_num, duration):
    print(f"started {task_num}")
    await asyncio.sleep(duration) 
    # 비동기 작업: 기다리는 동안 다른 일을 할 수 있어
    print(f"ended {task_num}") 

async def main():
    task1 = asyncio.create_task(\
        async_task(1,3))
    task2 = asyncio.create_task(\
        async_task(2,2))
    task3 = asyncio.create_task(\
        async_task(3,1))
                                
    await task1
    await task2
    await task3

async def gather_main():
    await asyncio.gather(
        async_task(1, 3),
        async_task(2, 2),
        async_task(3, 1),
    )

begin = time.time()
asyncio.run(main())
end = time.time()

print(f"Async time is {end - begin}") 
import asyncio
import time

# asynchronous function that calculates the partial sum of numbers from start to end
async def calculate_partial_sum(start, end):
    return sum(range(start, end + 1))

# main asynchronous function that distributes work and collects results
async def calculate_sum():
    total_tasks = 5  # total number of tasks
    n = 1000000  # upper bound of the range
    step = n // total_tasks  # step for dividing the range into parts
    tasks = []

    # create tasks for calculating partial sums
    for i in range(total_tasks):
        start = i * step + 1  # start of the range for the current task
        end = (i + 1) * step if i != total_tasks - 1 else n  # end of the range for the current task
        tasks.append(asyncio.create_task(calculate_partial_sum(start, end)))

    # wait for all tasks to complete and collect results
    results = await asyncio.gather(*tasks)
    total_sum = sum(results)  # sum up the results of all tasks
    return total_sum

start_time = time.time()
sum_result = asyncio.run(calculate_sum())  # run the asynchronous function
end_time = time.time()
print(f"sum: {sum_result}, time: {end_time - start_time} seconds")  # output the result and execution time

import threading
import time

# function that calculates the partial sum of numbers from start to end and writes the result to a shared list
def calculate_partial_sum(start, end, result, index):
    result[index] = sum(range(start, end + 1))

# function that distributes work between threads and collects results
def calculate_sum():
    total_threads = 5  # total number of threads
    n = 1000000  # upper bound of the range
    thread_list = []
    result = [0] * total_threads  # shared list for storing results

    # create threads for calculating partial sums
    for i in range(total_threads):
        start = i * (n // total_threads) + 1  # start of the range for the current thread
        end = (i + 1) * (n // total_threads) if i != total_threads - 1 else n  # end of the range for the current thread

        thread = threading.Thread(target=calculate_partial_sum, args=(start, end, result, i))
        thread_list.append(thread)
        thread.start()  # start the thread

    # wait for all threads to complete
    for thread in thread_list:
        thread.join()

    total_sum = sum(result)  # sum up the results of all threads
    return total_sum

start_time = time.time()
sum_result = calculate_sum()  # run the function
end_time = time.time()
print(f"sum: {sum_result}, time: {end_time - start_time} seconds")  # output the result and execution time

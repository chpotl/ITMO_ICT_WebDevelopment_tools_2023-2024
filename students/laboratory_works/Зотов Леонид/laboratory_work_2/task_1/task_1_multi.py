import multiprocessing
import time

# function that calculates the partial sum of numbers from start to end and writes the result to a shared list
def calculate_partial_sum(start, end, result, index):
    result[index] = sum(range(start, end + 1))

# function that distributes work between processes and collects results
def calculate_sum():
    total_processes = 5  # total number of processes
    n = 1000000  # upper bound of the range
    process_list = []
    manager = multiprocessing.Manager()
    result = manager.list([0] * total_processes)  # shared list for storing results

    # create processes for calculating partial sums
    for i in range(total_processes):
        start = i * (n // total_processes) + 1  # start of the range for the current process
        end = (i + 1) * (n // total_processes) if i != total_processes - 1 else n  # end of the range for the current process

        process = multiprocessing.Process(target=calculate_partial_sum, args=(start, end, result, i))
        process_list.append(process)
        process.start()  # start the process

    # wait for all processes to complete
    for process in process_list:
        process.join()

    total_sum = sum(result)  # sum up the results of all processes
    return total_sum

if __name__ == '__main__':
    start_time = time.time()
    sum_result = calculate_sum()  # run the function
    end_time = time.time()
    print(f"sum: {sum_result}, time: {end_time - start_time} seconds")  # output the result and execution time

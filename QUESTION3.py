

import threading  # Imports Python's built-in thread handling library
import time       # Imports the time library to track nanosecond precision clock values

# =====================================================================
# 1. FACTORIAL CALCULATION FUNCTION (Requirement #2)
# =====================================================================
def calculate_factorial(n):
    res = 1  # Step 1: Initialize the starting result variable to 1
    # Step 2: Loop from 1 up to the number 'n' (inclusive)
    for i in range(1, n + 1):
        res *= i  # Step 3: Multiply the current result value by the loop index 'i'
    return res  # Return the final calculated value back to the caller

# Array lists to hold the recorded execution times for all 10 rounds
multithread_round_times = []  # Stores time data for the multithreaded runs
sequential_round_times = []   # Stores time data for the single-threaded runs

# Target numbers array requested by the assignment details
numbers_to_calculate = [50, 100, 200]

# =====================================================================
# 2. EXPERIMENT 1: MULTITHREADING RUNS (Requirement #3)
# =====================================================================
print("=== STARTING MULTITHREADING BENCHMARK (10 ROUNDS) ===")

# Run an outer loop to repeat the entire experiment across exactly 10 separate rounds
for round_num in range(1, 11):
    thread_pool = []  # Temporary list container to keep track of active thread workers
    
    # Formula Component t1: Capture the start timestamp before the first thread fires
    t1 = time.perf_counter_ns()
    
    # Create and launch a separate independent thread for each target number
    for num in numbers_to_calculate:
        # Define a thread worker targeting our factorial function with arguments
        worker_thread = threading.Thread(target=calculate_factorial, args=(num,))
        thread_pool.append(worker_thread)  # Store thread reference in our tracking pool
        worker_thread.start()              # Tell the operating system to start executing the thread
        
    # Force the main master program to wait patiently for all 3 threads to finish up
    for worker_thread in thread_pool:
        worker_thread.join()  # Suspends execution until this specific thread completely finishes
        
    # Formula Component t2: Capture the end timestamp immediately after the final thread stops
    t2 = time.perf_counter_ns()
    
    # Calculate the elapsed time for this specific round: T = t2 - t1
    time_elapsed = t2 - t1
    multithread_round_times.append(time_elapsed)  # Save the time result to our history list
    print(f"Round {round_num:2d}: Time Elapsed (T) = {time_elapsed:,} ns")

# Compute the mathematical average for all 10 multithreaded rounds combined
average_multithread_time = sum(multithread_round_times) / 10
print(f"--> Average Multithreading Execution Time: {average_multithread_time:,} ns\n")

# =====================================================================
# 3. EXPERIMENT 2: SEQUENTIAL RUNS (Requirement #4)
# =====================================================================
print("=== STARTING SEQUENTIAL BENCHMARK (10 ROUNDS) ===")

# Run a matching outer loop to repeat the sequential experiment across 10 rounds
for round_num in range(1, 11):
    
    # Capture the start timestamp before any work begins for this round
    t1 = time.perf_counter_ns()
    
    # Linearly execute the calculations one after another on the main single thread
    for num in numbers_to_calculate:
        calculate_factorial(num)  # Runs completely to the end before stepping to the next line
        
    # Capture the final end timestamp after all three numbers finish calculating
    t2 = time.perf_counter_ns()
    
    # Calculate the elapsed time for this round: T = t2 - t1
    time_elapsed = t2 - t1
    sequential_round_times.append(time_elapsed)  # Save the time result to our sequential history list
    print(f"Round {round_num:2d}: Time Elapsed (T) = {time_elapsed:,} ns")

# Compute the mathematical average for all 10 sequential rounds combined
average_sequential_time = sum(sequential_round_times) / 10
print(f"--> Average Sequential Execution Time: {average_sequential_time:,} ns")

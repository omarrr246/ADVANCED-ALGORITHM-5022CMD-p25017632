
import time

# 1. SIMPLE TRANSACTION ENTITY CLASS (Requirement #2)
class Transaction:
    def __init__(self, id, name, amount):
        self.id = id          # Unique Transaction ID (Integer)
        self.name = name      # Customer Name (String)
        self.amount = amount  # Transaction Amount (Float)

# 2. MERGE SORT ALGORITHM (Requirement #1 & #4a)
def merge_sort(arr):
    if len(arr) <= 1: 
        return arr  # Base Case: A list of 1 or 0 items is already sorted

    # DIVIDE: Split the array right down the middle
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # CONQUER: Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # COMBINE: Merge the sorted pieces back together
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = 0  # Pointer index for the left list
    j = 0  # Pointer index for the right list

    # Compare items side-by-side and collect the smaller one
    while i < len(left) and j < len(right):
        if left[i].id < right[j].id:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining items left over from either side
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 3. BINARY SEARCH ALGORITHM (Requirement #1 & #4b)
def binary_search(arr, target, low, high):
    if low > high: 
        return -1  # Base Case: Target not found

    # DIVIDE: Find the middle element
    mid = (low + high) // 2

    # CONQUER: Check if mid is the target, otherwise discard half the list
    if arr[mid].id == target: 
        return mid
    elif arr[mid].id > target: 
        return binary_search(arr, target, low, mid - 1)  # Search left side
    else: 
        return binary_search(arr, target, mid + 1, high) # Search right side

# 4. LINEAR SEARCH ALGORITHM (Requirement #5 - Mandatory Feature d)
def linear_search(arr, target):
    # Check every single element one-by-one from start to finish
    for i in range(len(arr)):
        if arr[i].id == target: 
            return i
    return -1

# 5. INITIAL DATASET: EXACTLY 10 UNSORTED RECORDS (Requirement #3)
dataset = [
    Transaction(505, "Alice", 99.9),
    Transaction(101, "Bob", 45.0),
    Transaction(404, "Charlie", 12.5),
    Transaction(202, "David", 300.0),
    Transaction(808, "Emma", 150.2),
    Transaction(303, "Frank", 22.1),
    Transaction(909, "Grace", 85.5),
    Transaction(606, "Henry", 60.0),
    Transaction(707, "Isabella", 120.0),
    Transaction(111, "Jack", 19.9)
]

# State tracker to ensure we don't run binary search on unsorted data
sorted_data = None

# 6. MANDATORY MENU SYSTEM (Requirement #5)
while True:
    print("\n--- TRANSACTION SYSTEM ---")
    print("a) Display All Transactions")
    print("b) Sort Transactions (Merge Sort)")
    print("c) Search Transaction (Binary Search)")
    print("d) Search Transaction (Linear Search)")
    print("e) Exit")
    
    choice = input("Choice (a-e): ").strip().lower()

    if choice == 'a':
        # If we have sorted the data, display the sorted list. Otherwise display original dataset.
        current_list = sorted_data if sorted_data else dataset
        print("\n--- Current Records ---")
        for tx in current_list:
            print(f"ID: {tx.id} | Name: {tx.name} | Amount: ${tx.amount}")

    elif choice == 'b':
        print("\n--- Running Merge Sort ---")
        print("Before Sorting:", [tx.id for tx in dataset])
        
        start = time.perf_counter_ns()
        sorted_data = merge_sort(dataset)  # Run sort
        end = time.perf_counter_ns()
        
        print("After Sorting:", [tx.id for tx in sorted_data])
        print(f"Execution Time: {end - start} ns")

    elif choice == 'c':
        if not sorted_data:
            print("\nError: Please sort the data using option 'b' first!")
            continue
            
        print("\n--- Binary Search Engine ---")
        target_id = int(input("Enter ID to look for: "))
        
        start = time.perf_counter_ns()
        index = binary_search(sorted_data, target_id, 0, len(sorted_data) - 1)
        duration = time.perf_counter_ns() - start
        
        if index != -1:
            print(f"Found! Name: {sorted_data[index].name} | Amount: ${sorted_data[index].amount}")
        else:
            print("Transaction ID not found.")
        print(f"Binary Search Time: {duration} ns")

    elif choice == 'd':
        print("\n--- Linear Search Engine ---")
        target_id = int(input("Enter ID to look for: "))
        
        # We can run linear search on the original unsorted dataset
        start = time.perf_counter_ns()
        index = linear_search(dataset, target_id)
        duration = time.perf_counter_ns() - start
        
        if index != -1:
            print(f"Found! Name: {dataset[index].name} | Amount: ${dataset[index].amount}")
        else:
            print("Transaction ID not found.")
        print(f"Linear Search Time: {duration} ns")

    elif choice == 'e':
        print("Exiting application.")
        break
    else:
        print("Invalid choice.")

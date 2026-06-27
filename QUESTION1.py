

import time  # Imports the time module to measure search speeds in nanoseconds

# =====================================================================
# 1. PRODUCT ENTITY CLASS (Requirement #2)
# =====================================================================
class Medicine:
    # The constructor method initializes each new medicine object with its data
    def __init__(self, id, name, price):
        self.id = id         # Unique product identity key (Integer)
        self.name = name     # Name of the item (String)
        self.price = price   # Cost of the item (Float)

# =====================================================================
# 2. HASH TABLE WITH LINEAR PROBING (Requirement #1)
# =====================================================================
class PharmacyStore:
    # Initializes an empty hash table structure when a store is created
    def __init__(self):
        self.size = 10                  # Sets the total number of available slots (buckets)
        self.table = [None] * self.size  # Creates a 1D list containing 10 empty 'None' spaces

    # The Hash Function: Determines the starting index address for any ID
    def hash_id(self, id):
        return id % self.size  # Uses modulo arithmetic (remainder) to guarantee an index from 0 to 9

    # Inserts a medicine object into the correct table slot
    def insert(self, med):
        index = self.hash_id(med.id)  # Step 1: Calculate the ideal starting index
        
        # Linear Probing: While the current slot is taken, step forward to find an empty one
        while self.table[index] is not None:
            index = (index + 1) % self.size  # Move to the next index. % wraps it around back to 0 if it hits 10
            
        self.table[index] = med  # Step 2: Place the medicine object into the found empty slot

    # Searches for a medicine record by its ID
    def search(self, id):
        index = self.hash_id(id)  # Step 1: Calculate where the item should ideally look first
        start = index             # Save the starting index to prevent an infinite loop if table is full
        
        # Look through slots sequentially until hitting an empty 'None' slot
        while self.table[index] is not None:
            if self.table[index].id == id:  # If the item matches our target ID...
                return self.table[index]    # ...Return the found medicine object immediately
                
            index = (index + 1) % self.size  # Move to the next index slot (Linear Probing check)
            if index == start:               # If we probe all the way back around to the start...
                break                        # ...Stop searching to avoid an infinite loop
                
        return None  # Returns None if the loop hits an empty slot or finishes wrapping around without a match

# =====================================================================
# 3. MAIN COMMAND-LINE INVENTORY SYSTEM (Requirement #3)
# =====================================================================
store = PharmacyStore()  # Instantiates the custom Hash Table structure
array_store = []         # Instantiates a standard 1D Array List for comparative testing (Requirement #4)

# Predefined sample records inserted into both data structures (Requirement #2)
med1 = Medicine(101, "Paracetamol", 5.50)  # ID 101 hashes to slot 1 (101 % 10 = 1)
med2 = Medicine(102, "Vitamin C", 12.00)   # ID 102 hashes to slot 2 (102 % 10 = 2)
med3 = Medicine(103, "Cough Syrup", 8.50)   # ID 103 hashes to slot 3 (103 % 10 = 3)

# Populate the Hash Table
store.insert(med1)
store.insert(med2)
store.insert(med3)

# Populate the 1D Array with identical records
array_store.append(med1)
array_store.append(med2)
array_store.append(med3)

# Infinite loop to keep the Command Line Menu system running
while True:
    print("\n=== PHARMACY INVENTORY MENU ===")
    print("1. Display All Items")
    print("2. Insert New Product")
    print("3. Search Product by ID")
    print("4. Run Performance Comparison Experiment")
    print("5. Exit")
    
    choice = input("Select Option (1-5): ")  # Captures user menu choice
    
    # -----------------------------------------------------------------
    # CHOICE 1: DISPLAY SYSTEM DATA
    # -----------------------------------------------------------------
    if choice == "1":
        print("\n--- Current Inventory Status ---")
        # Loop through all 10 slots of the internal Hash Table array structure
        for i in range(10):
            if store.table[i]:  # If the slot contains a medicine object...
                print(f"Slot {i}: ID {store.table[i].id} - {store.table[i].name} (${store.table[i].price})")
            else:               # If the slot contains a 'None' value...
                print(f"Slot {i}: Empty")
                
    # -----------------------------------------------------------------
    # CHOICE 2: DYNAMIC INSERTION
    # -----------------------------------------------------------------
    elif choice == "2":
        print("\n--- Insert New Product ---")
        new_id = int(input("Enter Product ID: "))          # Read product ID integer input
        new_name = input("Enter Product Name: ")           # Read name text string input
        new_price = float(input("Enter Product Price: "))  # Read decimal float value input
        
        new_med = Medicine(new_id, new_name, new_price)  # Create new custom object
        store.insert(new_med)       # Insert into Hash Table (runs modulo calculation and places it)
        array_store.append(new_med) # Appends straight onto the end of the 1D comparison Array
        print("Product added successfully!")
        
    # -----------------------------------------------------------------
    # CHOICE 3: STANDARD SYSTEM LOOKUP
    # -----------------------------------------------------------------
    elif choice == "3":
        print("\n--- Search Product ---")
        search_id = int(input("Enter ID to search: "))  # Target ID query capture
        res = store.search(search_id)                    # Runs the custom internal hash probing lookups
        if res: 
            print(f"Found: {res.name} (Price: ${res.price})")
        else: 
            print("Product Not Found.")
            
    # -----------------------------------------------------------------
    # CHOICE 4: PERFORMANCE TESTING HARNESS (Requirement #4)
    # -----------------------------------------------------------------
    elif choice == "4":
        print("\n--- Running Performance Experiment ---")
        
        # -------------------------------------------------------------
        # TEST 1: Lookup execution speeds on an EXISTING key (ID: 101)
        # -------------------------------------------------------------
        # Measure Hash Table lookup speed
        start = time.perf_counter_ns()        # Get starting time stamp in nanoseconds
        store.search(101)                     # Executes hash lookup (Calculates address -> jumps directly)
        hash_time_exist = time.perf_counter_ns() - start  # Calculate difference duration

        # Measure 1D Array sequential search speed
        start = time.perf_counter_ns()        # Get starting time stamp in nanoseconds
        for item in array_store:               # For-loop sequentially scanning the list items
            if item.id == 101:                 # If the current matching ID is found...
                break                          # ...break out of loop instantly
        array_time_exist = time.perf_counter_ns() - start  # Calculate difference duration

        # -------------------------------------------------------------
        # TEST 2: Lookup execution speeds on a NON-EXISTING key (ID: 999)
        # -------------------------------------------------------------
        # Measure Hash Table failure tracking speed
        start = time.perf_counter_ns()        # Get starting time stamp
        store.search(999)                     # Runs address routing logic and safely stops
        hash_time_none = time.perf_counter_ns() - start   # Calculate difference duration
        
        # Measure 1D Array complete sequential linear search failure speed
        start = time.perf_counter_ns()        # Get starting time stamp
        for item in array_store:               # Must inspect every single record inside the system array
            if item.id == 999:                 # Checks if id matches target 999
                break                          # (Will never trigger because 999 does not exist)
        array_time_none = time.perf_counter_ns() - start  # Calculate total wasted lookup duration

        # Output the performance results
        print(f"1. Existing Key Lookup (ID 101):")
        print(f"   - Hash Table Search Time: {hash_time_exist} ns")
        print(f"   - 1D Array Search Time:  {array_time_exist} ns")
        print(f"2. Non-Existing Key Lookup (ID 999):")
        print(f"   - Hash Table Search Time: {hash_time_none} ns")
        print(f"   - 1D Array Search Time:  {array_time_none} ns")
        
        # Theoretical justification note for your assignment documentation analysis text
        print("\nExplanation: Hash Table remains consistently faster because it maps directly to an index position O(1), whereas the 1D Array has to loop through every single element sequentially O(N).")
        
    # -----------------------------------------------------------------
    # CHOICE 5: EXIT PROGRAM
    # -----------------------------------------------------------------
    elif choice == "5":
        print("Exiting Program.")
        break  # Terminate infinite menu execution loop safely
    else:
        print("Invalid choice. Try again.")

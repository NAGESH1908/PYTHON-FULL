import sys

def solve():
    """
    Determines the minimum number of cut-and-insert operations
    to restore the shuffled list to the original sequence using
    the Longest Increasing Subsequence (LIS) method.
    """
    try:
        # Read N, the number of instructions
        # Handle the case where N is not on the first line in Example 2
        # We'll read lines until we find a number
        n_line = sys.stdin.readline().strip()
        while not n_line.isdigit():
            n_line = sys.stdin.readline().strip()
            if not n_line: # Handle end of file
                 return
        
        N = int(n_line)
        
        # Read "shuffled" marker
        sys.stdin.readline() 
        
        # Read the N shuffled instructions
        shuffled_list = []
        for _ in range(N):
            shuffled_list.append(sys.stdin.readline().strip())
        
        # Read "original" marker
        sys.stdin.readline()
        
        # Read the N original instructions
        original_list = []
        for _ in range(N):
            original_list.append(sys.stdin.readline().strip())

    except Exception:
        # Handle potential EOF or format errors gracefully
        return

    # 1. Map each instruction string to its index in the original list
    # The index represents the correct final position.
    original_map = {instruction: i for i, instruction in enumerate(original_list)}

    # 2. Create the sequence of original indices (I) from the shuffled list
    # The LIS of this sequence I will tell us the maximum number of elements
    # already in correct relative order.
    index_sequence = []
    for instruction in shuffled_list:
        if instruction in original_map:
            index_sequence.append(original_map[instruction])

    # 3. Find the Length of the Longest Increasing Subsequence (LIS) of I
    # We use a standard O(N log N) algorithm for LIS.
    # The tails array stores the smallest tail of all increasing subsequences
    # with length i+1 at tails[i].
    tails = []
    for number in index_sequence:
        # Binary search for the smallest tail >= current number
        low, high = 0, len(tails)
        while low < high:
            mid = (low + high) // 2
            if tails[mid] < number:
                low = mid + 1
            else:
                high = mid
        
        # If the number is greater than all tails, extend the LIS (new tail)
        if low == len(tails):
            tails.append(number)
        # Otherwise, replace the tail of the sequence of length low+1
        else:
            tails[low] = number

    lis_length = len(tails)

    # 4. Calculate Minimum Operations
    # The minimum number of operations is N minus the length of the LIS.
    min_operations = N - lis_length

    print(min_operations)

# Execute the solve function
if _name_ == "_main_":
    solve()
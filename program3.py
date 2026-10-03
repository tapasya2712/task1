import time
from functools import lru_cache

def count_ways_recursive(n: int) -> int:
    
    # Base cases:
    if n == 0:
        return 1  # 1 way: stand at base (0 steps remaining)
    if n < 0:
        return 0  # 0 ways: invalid step count

    # Recursive relation: sum of ways from taking 1, 2, or 3 steps
    return (count_ways_recursive(n - 1) + 
            count_ways_recursive(n - 2) + 
            count_ways_recursive(n - 3))



def count_ways_memo(n: int, memo: dict = None) -> int:
    
    if memo is None:
        memo = {}

    # Base cases:
    if n == 0:
        return 1
    if n < 0:
        return 0

    # Return cached result if already computed
    if n in memo:
        return memo[n]

    # Compute and store result in memo dictionary
    memo[n] = (count_ways_memo(n - 1, memo) + 
               count_ways_memo(n - 2, memo) + 
               count_ways_memo(n - 3, memo))

    return memo[n]



@lru_cache(maxsize=None)
def count_ways_lru(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_ways_lru(n - 1) + count_ways_lru(n - 2) + count_ways_lru(n - 3)



if __name__ == "__main__":
    # Verification with sample input n = 4
    print("=== Verification (Input: n = 4) ===")
    print(f"count_ways_recursive(4) = {count_ways_recursive(4)}")  # Output: 7
    print(f"count_ways_memo(4)      = {count_ways_memo(4)}")       # Output: 7
    print(f"count_ways_lru(4)       = {count_ways_lru(4)}")        # Output: 7

    # Performance Benchmark for n = 30
    n = 30
    print(f"\n=== Performance Benchmark (Input: n = {n}) ===")

    # 1. Measure Plain Recursion
    start_time = time.perf_counter()
    ans_rec = count_ways_recursive(n)
    end_time = time.perf_counter()
    time_rec = end_time - start_time
    print(f"Plain Recursion Result : {ans_rec}")
    print(f"Plain Recursion Time   : {time_rec:.6f} seconds")

    # 2. Measure Memoized Recursion
    start_time = time.perf_counter()
    ans_memo = count_ways_memo(n)
    end_time = time.perf_counter()
    time_memo = end_time - start_time
    print(f"Memoized Result        : {ans_memo}")
    print(f"Memoized Time          : {time_memo:.8f} seconds")

    if time_memo > 0:
        speedup = time_rec / time_memo
        print(f"\nMemoization is approximately {speedup:,.2f}x faster for n = {n}!")

import time
from functools import lru_cache


memo = {1: 0}


def collatz_steps(n: int) -> int:
    
    # Return memoized result if available
    if n in memo:
        return memo[n]

    # Calculate next term in sequence
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1

    # Recursive call: 1 + steps required for next_n
    memo[n] = 1 + collatz_steps(next_n)
    return memo[n]



@lru_cache(maxsize=None)
def collatz_steps_lru(n: int) -> int:
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + collatz_steps_lru(n // 2)
    else:
        return 1 + collatz_steps_lru(3 * n + 1)



def main():
    # 1. Verify required test input n = 27
    input_val = 27
    steps_27 = collatz_steps(input_val)
    print(f"Input: {input_val}")
    print(f"Output: {steps_27} steps\n")

    # 2. Find the number between 1 and 10,000 with the longest chain
    limit = 10000
    max_number = 1
    max_steps = 0

    start_time = time.perf_counter()
    for i in range(1, limit + 1):
        steps = collatz_steps(i)
        if steps > max_steps:
            max_steps = steps
            max_number = i
    end_time = time.perf_counter()

    # 3. Print Results
    print(f"--- Range [1 to {limit:,}] Results ---")
    print(f"Number with longest chain : {max_number}")
    print(f"Number of steps           : {max_steps} steps")
    print(f"Execution time            : {(end_time - start_time) * 1000:.2f} ms")
    print(f"Total unique states cached: {len(memo):,}")


if __name__ == "__main__":
    main()

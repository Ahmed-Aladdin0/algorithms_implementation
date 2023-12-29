import time


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Count array for digits 0 to 9

    # Count occurrences of each digit at the current place value
    for i in range(n):
        index = (arr[i] // exp)
        count[index % 10] += 1

    # Update count array to store cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using the count array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    print("Radix sort!")
    start = time.time()
    startP = time.process_time()
    # Find the maximum number to determine the number of digits
    max_num = max(arr)

    # Perform counting sort for each digit place value
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    print(arr)
    finish = time.time()
    finishP = time.process_time()
    elapsed = finish - start
    cpu = finishP - startP
    print('Real time:', elapsed, 'seconds')
    print('CPU time:', cpu, 'seconds')
    print()

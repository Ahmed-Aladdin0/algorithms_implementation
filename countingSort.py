import time


def counting_sort(arr):
    print("Counting sort!")
    start = time.time()
    startP = time.process_time()
    # Find the maximum value in the array
    max_val = max(arr)

    # Create a count array to store the frequency of each element
    count = [0] * (max_val + 1)

    # Count the occurrences of each element
    for num in arr:
        count[num] += 1

    # Update the count array to store the cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create the output array
    output = [0] * len(arr)

    # Build the output array based on the count array
    for num in reversed(arr):
        index = count[num] - 1
        output[index] = num
        count[num] -= 1

    print(arr)
    finish = time.time()
    finishP = time.process_time()
    elapsed = finish - start
    cpu = finishP - startP
    print('Real time:', elapsed, 'seconds')
    print('CPU time:', cpu, 'seconds')
    print()
    return output



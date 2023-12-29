import time


def quick_sort(arr, print_sorted=True, print_time=True, start=None, startP=None):
    if print_time and start is None:
        start = time.time()
        startP = time.process_time()

    if len(arr) <= 1:
        return arr
    else:
        # Choose pivot as the median of the first, middle, and last elements
        pivot_index = (0 + len(arr) - 1) // 2
        pivot = sorted([arr[0], arr[pivot_index], arr[-1]])[1]

        less_than_pivot = [x for x in arr if x < pivot]
        equal_to_pivot = [x for x in arr if x == pivot]
        greater_than_pivot = [x for x in arr if x > pivot]

        sorted_array = quick_sort(less_than_pivot, print_sorted=False, print_time=False, start=start) + equal_to_pivot + quick_sort(greater_than_pivot, print_sorted=False, print_time=False, start=start)

        if print_sorted:
            print("Quick sort!")
            print(sorted_array)

        if print_time and start is not None:
            finish = time.time()
            finishP = time.process_time()
            elapsed = finish - start
            cpu = finishP - startP
            print('Real time:', elapsed, 'seconds')
            print('CPU time:', cpu, 'seconds')
            print()

        return sorted_array

import time


def merge_sort(arr, print_time=True):

    global start, startP
    if print_time:
        start = time.time()  # Record the start time
        startP = time.process_time()

    def merge(arr, left, right):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy the remaining elements of left and right, if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on the left and right halves
        merge_sort(left_half, print_time=False)
        merge_sort(right_half, print_time=False)

        # Merge the sorted halves
        merge(arr, left_half, right_half)

    if print_time:
        print("Merge sort!")
        print(arr)
        finish = time.time()
        finishP = time.process_time()
        elapsed = finish - start
        cpu = finishP - startP
        print('Real time:', elapsed, 'seconds')
        print('CPU time:', cpu, 'seconds')
        print()


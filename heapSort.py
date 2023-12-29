import time

def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child exists and is greater than the root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child exists and is greater than the root
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Swap the root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    print("Heap sort!")
    start = time.time()
    startP = time.process_time()
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)
    print(arr)
    finish = time.time()
    finishP = time.process_time()
    elapsed = finish - start
    cpu = finishP - startP
    print('Real time:', elapsed, 'seconds')
    print('CPU time:', cpu, 'seconds')
    print()

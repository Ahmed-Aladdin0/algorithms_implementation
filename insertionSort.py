import time


def insertion_Sort(arr):
    print("Insertion sort!")
    start = time.time()
    startP = time.process_time()
    for i in range(1, len(arr)):
        key = arr[i]
        while arr[i-1] > key and i > 0:
            arr[i] = arr[i-1]
            arr[i-1] = key
            i = i-1


    print(arr)
    finish = time.time()
    finishP = time.process_time()
    elapsed = finish - start
    cpu = finishP - startP
    print('Real time:' , elapsed , 'seconds')
    print('CPU time:', cpu , 'seconds')
    print()



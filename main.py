import random
import insertionSort
import heapSort
import mergeSort
import countingSort
import radixSort
import quickSort
import matrixMultiplicatoin

mRand1 = matrixMultiplicatoin.generate_random_matrix(8, 8)
mRand2 = matrixMultiplicatoin.generate_random_matrix(8, 8)

aRandom = []
aSorted = []
aReverse = []

for i in range(0,10000):
    aRandom.append(random.randint(0,1000000))

for i in range(1,10000):
    aSorted.append(i)

for i in range(10000,1,-1):
    aReverse.append(i)


print()

print("Sorting random array")
insertionSort.insertion_Sort(aRandom)
print("Sorting sorted array")
insertionSort.insertion_Sort(aSorted)
print("Sorting reversed array")
insertionSort.insertion_Sort(aReverse)
print("---------------------------------------------------------------------------------------------------------------")

print("Sorting random array")
heapSort.heap_sort(aRandom)
print("Sorting sorted array")
heapSort.heap_sort(aSorted)
print("Sorting reversed array")
heapSort.heap_sort(aReverse)

print("---------------------------------------------------------------------------------------------------------------")

print("Sorting random array")
mergeSort.merge_sort(aRandom)
print("Sorting sorted array")
mergeSort.merge_sort(aSorted)
print("Sorting reversed array")
mergeSort.merge_sort(aReverse)

print("---------------------------------------------------------------------------------------------------------------")

print("Sorting random array")
countingSort.counting_sort(aRandom)
print("Sorting sorted array")
countingSort.counting_sort(aSorted)
print("Sorting reversed array")
countingSort.counting_sort(aReverse)

print("---------------------------------------------------------------------------------------------------------------")

print("Sorting random array")
radixSort.radix_sort(aRandom)
print("Sorting sorted array")
radixSort.radix_sort(aSorted)
print("Sorting reversed array")
radixSort.radix_sort(aReverse)

print("---------------------------------------------------------------------------------------------------------------")

print("Sorting random array")
quickSort.quick_sort(aRandom)
print("Sorting sorted array")
quickSort.quick_sort(aSorted)
print("Sorting reversed array")
quickSort.quick_sort(aReverse)

print("---------------------------------------------------------------------------------------------------------------")

matrixMultiplicatoin.strassen_matrix_multiplication(mRand1, mRand2)



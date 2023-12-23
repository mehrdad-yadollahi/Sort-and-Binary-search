
#Just run the below Program

import random
import time

# Function to generate random data and save to a file
def generate_random_data(size):
    data = [random.randint(0, 1000) for _ in range(size)]
    with open(f'random_data_{size}.txt', 'w') as file:
        for number in data:
            file.write(f"{number}\n")

# Function to generate sorted random data and save to a file
def generate_sorted_data(size):
    data = sorted([random.randint(0, 1000) for _ in range(size)])
    with open(f'sorted_data_{size}.txt', 'w') as file:
        for number in data:
            file.write(f"{number}\n")

# Function to generate reverse sorted data and save to a file
def generate_reverse_sorted_data(size):
    data = sorted([random.randint(0, 1000) for _ in range(size)], reverse=True)
    with open(f'reverse_sorted_data_{size}.txt', 'w') as file:
        for number in data:
            file.write(f"{number}\n")

# Function to generate identical data and save to a file
def generate_identical_data(size):
    data = [random.randint(0, 1000) for _ in range(size)]
    identical_number = random.randint(0, 1000)
    data = [identical_number] * size
    with open(f'identical_data_{size}.txt', 'w') as file:
        for number in data:
            file.write(f"{number}\n")

# Insertion Sort
def insertion_sort(arr):
    comparisons = 0
    start_time = time.time()
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
            comparisons += 1
        arr[i + 1] = key
    execution_time = (time.time() - start_time) * 1000
    return comparisons, execution_time


# Merge Sort
def merge_sort(arr):
    comparisons = 0
    start_time = time.time()

    def merge(arr, p, q, r):
        left = arr[p:q + 1]
        right = arr[q + 1:r + 1]
        left.append(float('inf'))
        right.append(float('inf'))
        i = j = 0

        nonlocal comparisons
        for k in range(p, r + 1):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                comparisons += len(left) - 1 - i

    def merge_sort_helper(arr, p, r):
        if p < r:
            q = (p + r) // 2
            merge_sort_helper(arr, p, q)
            merge_sort_helper(arr, q + 1, r)
            merge(arr, p, q, r)

    merge_sort_helper(arr, 0, len(arr) - 1)

    execution_time = (time.time() - start_time) * 1000
    return comparisons, execution_time


# Heap Sort
def heap_sort(arr):
    comparisons = 0
    start_time = time.time()

    def max_heapify(arr, i, heap_size):
        nonlocal comparisons
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < heap_size and arr[left] > arr[largest]:
            largest = left
        comparisons += 1

        if right < heap_size and arr[right] > arr[largest]:
            largest = right
        comparisons += 1

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            max_heapify(arr, largest, heap_size)

    def build_max_heap(arr):
        for i in range(len(arr) // 2, -1, -1):
            max_heapify(arr, i, len(arr))

    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)

    execution_time = (time.time() - start_time) * 1000
    return comparisons, execution_time

# 4-way Merge Sort
def merge_sort_4(arr):
    comparisons = 0
    start_time = time.time()

    def merge(arr, p, q1, q2, q3, r):
        left = arr[p:q1 + 1]
        middle1 = arr[q1 + 1:q2 + 1]
        middle2 = arr[q2 + 1:q3 + 1]
        right = arr[q3 + 1:r + 1]

        left.append(float('inf'))
        middle1.append(float('inf'))
        middle2.append(float('inf'))
        right.append(float('inf'))

        i = j = k = l = 0

        nonlocal comparisons
        for m in range(p, r + 1):
            min_val = min(left[i], middle1[j], middle2[k], right[l])
            arr[m] = min_val

            if min_val == left[i]:
                i += 1
            elif min_val == middle1[j]:
                j += 1
                comparisons += len(left) - 1 - i
            elif min_val == middle2[k]:
                k += 1
                comparisons += len(left) + len(middle1) - 2 - i - j
            else:
                l += 1
                comparisons += len(left) + len(middle1) + len(middle2) - 3 - i - j - k

    def merge_sort_4_helper(arr, p, r):
        if r - p <= 3:
            return
        q1 = p + (r - p) // 4
        q2 = p + 2 * (r - p) // 4
        q3 = p + 3 * (r - p) // 4

        merge_sort_4_helper(arr, p, q1)
        merge_sort_4_helper(arr, q1 + 1, q2)
        merge_sort_4_helper(arr, q2 + 1, q3)
        merge_sort_4_helper(arr, q3 + 1, r)

        merge(arr, p, q1, q2, q3, r)

    merge_sort_4_helper(arr, 0, len(arr) - 1)

    execution_time = (time.time() - start_time) * 1000
    return comparisons, execution_time

# Function to read data from a file
def read_data(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

# Function to run and print results
def run_and_print(algorithm, data_filename, size):
    data = read_data(data_filename)
    comparisons, execution_time = algorithm(data)
    print(f"{size}, {comparisons}, {execution_time:.0f}")

# Generate input data files
sizes = [15000, 30000, 60000, 120000, 240000]
for size in sizes:
    generate_random_data(size)
    generate_sorted_data(size)
    generate_reverse_sorted_data(size)
    generate_identical_data(size)

# Run algorithms and print results
algorithms = [insertion_sort, merge_sort, heap_sort, merge_sort_4]
for algorithm in algorithms:
    for size in sizes:
        for data_type in ['random', 'sorted', 'reverse_sorted', 'identical']:
            data_filename = f'{data_type}_data_{size}.txt'
            run_and_print(algorithm, data_filename, size)

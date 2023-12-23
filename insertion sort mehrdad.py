import random
import time

# Step 1: Generate input data sets
def generate_data(size):
    data = [random.randint(0, 1000000) for _ in range(size)]
    return data

sizes = [15000, 30000, 60000, 120000, 240000]
categories = ['random', 'sorted', 'reverse_sorted', 'identical']

for size in sizes:
    for category in categories:
        data = []
        if category == 'random':
            data = generate_data(size)
        elif category == 'sorted':
            data = sorted(generate_data(size))
        elif category == 'reverse_sorted':
            data = sorted(generate_data(size), reverse=True)
        elif category == 'identical':
            data = [random.randint(0, 1000000)] * size
        with open(f'{category}_{size}.txt', 'w') as file:
            for number in data:
                file.write(f"{number}\n")

# Step 2: Implement insertion sort algorithm
def insertion_sort(arr):
    comparisons = 0
    start_time = time.time()
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            comparisons += 1
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # in milliseconds
    return comparisons, execution_time

# Step 3 and 4: Analyze and report performance
for size in sizes:
    for category in categories:
        with open(f'{category}_{size}.txt', 'r') as file:
            input_data = [int(line.strip()) for line in file]
        comparisons, execution_time = insertion_sort(input_data)
        print(f"{size},{comparisons},{execution_time}")

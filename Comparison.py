import random
import time


# === Book Record Generator ===
def generate_book_record():
    isbn = random.randint(100000, 999999)
    return isbn


# === Linear Search ===
def linear_search(records, isbn_target):
    for record in records:
        if record == isbn_target:
            return record
    return None


# === Merge Sort ===
def merge_sort(records):
    if len(records) <= 1:
        return records
    mid = len(records) // 2
    left = merge_sort(records[:mid])
    right = merge_sort(records[mid:])
    return merge(left, right)


def merge(left, right):
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# === Binary Search ===
def binary_search(records, isbn_target):
    low, high = 0, len(records) - 1
    while low <= high:
        mid = (low + high) // 2
        if records[mid] == isbn_target:
            return records[mid]
        elif records[mid] < isbn_target:
            low = mid + 1
        else:
            high = mid - 1
    return None


# === Experiment Execution ===
def main():
    num_records = 80000
    records = [generate_book_record() for _ in range(num_records)]

    # Time merge sort
    start_time = time.time()
    sorted_records = merge_sort(records)
    merge_sort_time = (time.time() - start_time) * 1000

    # Compare Linear search vs Binary search 5000 times
    for _ in range(5000):
        isbn_target = random.randint(100000, 999999)

        start_time = time.time()
        linear_search(records, isbn_target)
        linear_search_time = (time.time() - start_time) * 1000

        start_time = time.time()
        binary_search(sorted_records, isbn_target)
        binary_search_time = (time.time() - start_time) * 1000
        total_time_binary = merge_sort_time + binary_search_time

        cheaper_search_flag = 1 if total_time_binary < linear_search_time else 0

        # You can print both linear and binary results if needed
        # print(f"{num_records}, {int(linear_search_time * 1000000)}, {cheaper_search_flag}")
        print(f"{num_records}, {int(total_time_binary * 1000000)}, {cheaper_search_flag}")


if __name__ == "__main__":
    main()

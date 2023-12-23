import random
import time


# === Book Record Generator ===
def generate_book_record():
    isbn = random.randint(100000, 999999)
    return isbn


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
            return mid
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
    merge_sort_time = (time.time() - start_time) * 10**9  # convert to nanoseconds

    for _ in range(5000):
        isbn_target = random.randint(100000, 999999)

        # Time binary search
        start_time = time.time()
        binary_search(sorted_records, isbn_target)
        binary_search_time = (time.time() - start_time) * 10**9  # convert to nanoseconds

        # Combine merge sort and binary search times
        total_time = merge_sort_time + binary_search_time
        print(f"{num_records}, {int(total_time)}")


if __name__ == "__main__":
    main()

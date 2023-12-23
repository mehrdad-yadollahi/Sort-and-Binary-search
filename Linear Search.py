import random
import string
import time

# === Book Record Generator ===
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_book_record():
    isbn = random.randint(100000, 999999)
    last_name = random_string(random.randint(3, 6))
    first_name = random_string(random.randint(3, 6))
    title = random_string(random.randint(4, 8))
    size_in_bytes = random.randint(100000, 999999)
    pointer_to_ebook = random.randint(1000000000, 9999999999)
    return f"{isbn},{last_name},{first_name},{title},{size_in_bytes},{pointer_to_ebook}"

# === Linear Search ===
def get_isbn(book_record):
    return int(book_record.split(',')[0])

def linear_search(records, isbn_target):
    for record in records:
        if get_isbn(record) == isbn_target:
            return record
    return None

# === Experiment Execution and Output ===
def time_linear_search(records, num_searches=1):
    # Linear Search
    start_time = time.time()
    for _ in range(num_searches):
        isbn_target = random.randint(100000, 999999)
        linear_search(records, isbn_target)
    linear_search_time = (time.time() - start_time) * 10**9
    return linear_search_time

def main():
    num_records = 800000
    records = [generate_book_record() for _ in range(num_records)]

    for _ in range(5000):  # Repeating the process 5000 times
        linear_time = time_linear_search(records, 1)  # We're only doing 1 search per iteration for 5000 iterations
        print(f"{num_records}, {int(linear_time)}")

if __name__ == "__main__":
    main()

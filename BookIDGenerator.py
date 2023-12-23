import random
import string


def random_string(length):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_book_record():
    """Generate a book record with random values."""
    isbn = random.randint(100000, 999999)
    last_name = random_string(random.randint(3, 6))
    first_name = random_string(random.randint(3, 6))
    title = random_string(random.randint(4, 8))
    size_in_bytes = random.randint(100000, 999999)
    pointer_to_ebook = random.randint(1000000000, 9999999999)

    # Return the book record as a string
    return f"{isbn},{last_name},{first_name},{title},{size_in_bytes},{pointer_to_ebook}"


def main():
    number_of_books = 20000
    filename = "books_records.txt"

    with open(filename, 'w') as file:
        for _ in range(number_of_books):
            book_record = generate_book_record()
            file.write(book_record + '\n')

    print(f"{number_of_books} book records have been written to {filename}.")


if __name__ == "__main__":
    main()

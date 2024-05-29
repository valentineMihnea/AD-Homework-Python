# Random and time for generating random pages and book counts
import random
import time

# Function to divide books among employees
def divide_books(books, num_books, num_employees):
    # Get the sum of all the books' pages
    total_pages = sum(books)
    # Calculate the ideal number of pages an employee should read, as the total number of pages divided by the number of employees
    ideal_pages = total_pages / num_employees
    read_pages = 0
    # Start with the first employee.
    current_employee = 1

    for i in range(num_books):
        # Calculate how many pages the current employee has read
        read_pages += books[i]
        # Print them to the console
        print(f"{books[i]} ", end="")
        # Because,later, we look at the next book, we need to check if we even have a next book.
        if i + 1 < num_books:
            # Calculate how many pages the employee would read if he read the next book.
            to_be_read_pages = read_pages + books[i + 1]
            # If reading the next book would put him above the ideal number of pages:
            if to_be_read_pages > ideal_pages:
                # We calculate the difference between the pages he already read and the ideal pages
                read_ideal_diff = ideal_pages - read_pages
                # We calculate the difference between the pages he will read next and the ideal pages
                to_be_read_ideal_diff = to_be_read_pages - ideal_pages
                # If reading the next book would put him closer to the number of ideal pages, then continue and reiterate to the next book
                if to_be_read_ideal_diff < read_ideal_diff:
                    continue
                # If not, print "- ", reset read pages to 0 and go to the next employee, unless this is the last employee
                else:
                    if current_employee < num_employees:
                        print("- ", end="")
                        read_pages = 0
                        current_employee += 1

# Function to create a random number of books
def randomize_books(min_number, max_number):
    random.seed(time.time())
    return random.randint(min_number, max_number)

# Function to create a random number of pages
def randomize_pages(num_books, min_number, max_number):
    random.seed(time.time())
    return [random.randint(min_number, max_number) for _ in range(num_books)]

def main():
    # Our number of employees.
    num_employees = 3
    # 0 - no random pages and book counts, 1 - random pages and book counts
    random_input = 1
    # Variables that set the minimum and maximum possible values of the random inputs
    min_random_books = 3
    max_random_books = 21
    min_random_pages = 1
    max_random_pages = 500

    # If we desire a random amount of books and pages
    if random_input == 1:
        num_books = randomize_books(min_random_books, max_random_books)
        books = randomize_pages(num_books, min_random_pages, max_random_pages)
        divide_books(books, num_books, num_employees)
    
    # If we want a pre-determined amount of books and pages
    else:
        books = [100, 200, 300, 400, 500, 600, 700, 800, 900]
        num_books = len(books)
        divide_books(books, num_books, num_employees)

if __name__ == "__main__":
    main()

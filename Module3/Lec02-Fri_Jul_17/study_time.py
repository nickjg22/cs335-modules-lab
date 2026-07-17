# library_search.py

library_catalog = [
    "Algorithms in Practice",
    "Clean Code",
    "Computer Networks",
    "Data Structures Made Clear",
    "Design Patterns",
    "Designing Programs",
    "Hacker's Delight",
    "How To Design Programs",
    "Introduction to Python",
    "More Programming Pearls",
    "Programming Patterns",
    "Programming Pearls",
    "Software Engineering Basics",
    "The Art of Computer Programming",
    "The C Programming Language",
    "The Little Schemer",
    "The Mythical Man-Month",
    "The Pragmatic Programmer",
    "Think Like a Programmer",
]


def binary_search_book(book_titles: list[str], target_title: str) -> int:
    """
    Return the index of target_title if it is in book_titles.

    If target_title is not present, return the index where it should be
    inserted to keep book_titles alphabetically sorted.
    """
    # YOUR CODE HERE
    pass  # Erase this line when you add your own code


def describe_result(book_titles: list[str], target_title: str) -> None:
    index = binary_search_book(book_titles, target_title)

    if index < len(book_titles) and book_titles[index] == target_title:
        print(f"Found '{target_title}' at index {index}.")
    else:
        print(f"'{target_title}' was not found.")
        print(f"It belongs at index {index}.")


describe_result(library_catalog, "Hacker's Delight")
describe_result(library_catalog, "Operating Systems")

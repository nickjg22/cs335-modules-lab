# broken_search.py

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


def find_book_position(book_titles: list[str], target_title: str) -> int:
    """
    Return the index of target_title if it is present.

    If target_title is missing, return the index where it should be inserted
    to keep book_titles alphabetically sorted.
    """
    low = 0
    high = len(book_titles) - 1

    while low < high:
        middle = (low + high) // 2

        if book_titles[middle] == target_title:
            return middle
        elif book_titles[middle] < target_title:
            low = middle
        else:
            high = middle

    return low


def describe_result(target_title: str) -> None:
    position = find_book_position(library_catalog, target_title)

    if position < len(library_catalog) and library_catalog[position] == target_title:
        print(f"Found '{target_title}' at index {position}.")
    else:
        print(f"'{target_title}' was not found.")
        print(f"It belongs at index {position}.")


describe_result("Algorithms in Practice")
describe_result("Data Structures Made Clear")
describe_result("Operating Systems")

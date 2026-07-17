CS335 - Friday, July 17 - Lecture 2 - Module 3

# Topics:
* [Code Lab Instructions](#code-lab-instructions)
* [Code Lab Challenge #0 - Choose the Study Time with Maximum Attendance](#code-lab-challenge-0---choose-the-study-time-with-maximum-attendance)
* [Code Lab Challenge #1 - Binary Search with Library Books](#code-lab-challenge-1---binary-search-with-library-books)
* [Code Lab Challenge #2 - Dijkstra's Algorithm by Hand](#code-lab-challenge-2---dijkstras-algorithm-by-hand)
* [Code Lab Challenge #3 - Implement Dijkstra's algorithm to Find the Shortest Route](#code-lab-challenge-3---implement-dijkstras-algorithm-to-find-the-shortest-route)
* [Code Lab Challenge #4 - Repair My Binary Search](#code-lab-challenge-4---repair-my-binary-search)


------------------------------------------------------------
# Announcements

### Attendance Policy

Beginning this week, in order for your attendance to be counted **you must reply to this week's Canvas discussion with the URL to your GitHub repository containing evidence of earnest participation.**

Last week, I was lenient and awarded participation points to students I remembered being present. However, that will not be reliable going forward (I am getting old). **You must post a reply in this discussion to be counted. Even if you were present, you will not receive credit without linking to a GitHub repository showing evidence of active participation in today's activities.

1.  You can create a new Git repo for this week, or re-use the repo from last time.
1.  Post the URL to your repo in a reply to this discussion.
1.  Engage with the activity by writing Markdown files in your GitHub repo.
    1.  You may add any other files, Python scripts, etc.
    1.  I will not regard a repo containing only a sparse README.md as evidence of attendance.
    1.  You must demonstrate evidence of active engagement with the activities.
1.  Commit all files and push to your upstream GitHub repo.
    1.  Ensure that your repo is visible to me, either by making it public OR creating it under the Ensign-College GitHub organization.


# Action Items

0.  Opening Prayer
0.  Spiritual Thought by Bro. Santos
0.  Introduce our new TA
0.  Stand-Up Meeting
0.  Code Challenges
0.  Break
0.  Code Challenges
0.  Wrap Up & Parting Thoughts


# Code Lab Instructions

Today's session consists of four coding labs. You will work in the same group
through all of the labs, and each teammate will rotate their role between each.
Before running any code, each teammate first makes an individual prediction.
Teams then compare reasoning, implement or repair code, and verify the result
with evidence.

Today's topical learning goals are:

* event-based maximum overlap & greedy interval selection
* binary search
* Dijkstra's shortest-path algorithm


## Group Rules

The maximum group size is *four*.

Members rotate roles at the start of every challenge:

* **Navigator:** defines the plan and proposes the next algorithmic step.
* **Reporter:** records the group's reasoning and is the spokesperson in the oral reports.
* **Driver:** controls the keyboard and writes shared code.
* **Verifier:** checks predictions, traces, and tests edge cases.

For *groups of three*, combine **navigator with reporter**.

For *pairs*, combine **driver with reporter** and **navigator with verifier**.


## Code Lab Workflow

Every code lab challenge follows this sequence of phases:

0. **Predict:** every team member writes their own expected result before execution.
1. **Discuss:** team members compare their predictions and identify disagreements.
2. **Implement or repair:** the driver edits code while the navigator explains each change.
3. **Verify:** the verifier checks the output against a trace, table, or edge case.
4. **Explain:** the reporter records one claim and the evidence supporting it.

**IMPORTANT - No group may run their program before every member has made a prediction!**


# Code Lab Challenge #0 - Choose the Study Time with Maximum Attendance

In this challenge you will help a study group choose the best meeting time.
Each student provides a time interval when they are available. Your program will
find the interval during which the greatest number of students can attend.

*Note: Students with deeper programming experience can try the stretch challenges in
Phase 4.*


### Program Requirements

0. Store each student's availability as a tuple containing a start time and an end time.
1. Define the body of the function `find_best_study_time` that accepts the availability intervals.
2. Find the greatest number of students available at the same time.
3. Return the earliest time interval with the greatest attendance.
4. Report the best interval and the number of students who can attend.
5. Use an event-based approach: process each interval's start and end rather than
   checking every possible time separately.
6. Do not assume that the intervals are already sorted.

Use *half-open intervals*: a student is available at the start time but is no longer
available at the end time. For example, `(9, 10)` and `(10, 11)` **do not overlap**.

For this challenge, all times are whole numbers and every interval has `start < end`.


<details>
<summary><h3>study_time.py</h3></summary>

```python
# study_time.py

availability = [
    (9, 11),
    (10, 12),
    (8, 11),
    (10, 13),
    (7, 11),
    (11, 14),
    (9, 15)
]


def find_best_study_time(availability: list[tuple[int, int]]) -> tuple[int, int, int]:
    """
    Return (start_time, end_time, attendance) for the earliest interval
    with the greatest number of available students.
    """
    # YOUR CODE HERE
    pass  # Erase this line when you add your own code


best_start, best_end, attendance = find_best_study_time(availability)
print(f"Best study time: {best_start}-{best_end}")
print(f"Expected attendance: {attendance} students")
```

</details>

Download [study_time.py](./study_time.py)


### Phase 0 - Predict

Create the file `challenge0.md` in your GitHub repo.

Work in a stable group with rotating roles: *driver*, *navigator*, *verifier*, and *reporter*.  You must take on a different role for each challenge. Note your role for this challenge in `challenge0.md`.

Before discussing the problem with your group, predict the best interval and
attendance individually, and write your prediction in `challenge0.md`.
**Do not run the program until every group member has recorded a prediction.**

Write answers to these questions in `challenge0.md`:

0.  What events happen at the start and end of each availability interval?
0.  What information must the program keep while it processes the events?


### Phase 1 - Discuss

*Navigator* facilitates the discussion as team members compare their predictions.

*Reporter* notes any disagreements.


### Phase 2 - Implement

Under the direction of the *navigator*, the *driver* writes pseudocode in a code block in `challenge0.md`.  Surround it with Python fences, like this:

~~~
```python
# your code goes here
...
pass
```
~~~

Your pseudocode should explain how to:

0. Convert the availability intervals into start and end events.
1. Sort the events by time.
2. Process events while maintaining the current attendance count.
3. Identify the time interval between consecutive event times.
4. Record a new best interval when the attendance increases to a new maximum.

With the help of the *navigator*, the *driver* refines the pseudocode until it approaches line-for-line equivalence with Python code.  The *verifier* checks their accuracy.

Then, the *driver* copies pseudocode from the team's `challenge0.md` files into the starter code file, and comments it out. Under the guidance of the *navigator*, the *driver* replaces each comment with runnable Python code until the program is complete.

### Phase 3 - Verify

Run the program with several availability lists. The *verifier* ensures that these cases are checked:

* everyone is available during the same interval
* one interval is completely inside another
* several intervals start at the same time
* one interval ends exactly when another begins
* multiple intervals tie for maximum attendance

When a start and an end occur at the same time, process the ending interval first.  This follows the half-open interval rule.

The *verifier* creates an event table that independently verifies the program's
maximum attendance and tie-breaking behavior.


### Phase 4 - Explain

All members answer these debrief questions in their own `challenge0.md`:

* How did the attendance count change as you processed each event?
* Why does the program process an ending interval before a starting interval at the same time?
* Why is it unnecessary to check every individual time between two event times?
* What input would help you discover a boundary error in your program?
* What is the time complexity of your approach in terms of the number of intervals?

The *reporter* prepares to share one claim and the evidence supporting it to the entire class.


### Five-Minute Greedy Mini-Task

Before moving to the next coding lab, use the same study-session context for this
short comparison. Given candidate study sessions represented as `(start_time,
end_time)`, choose the maximum number of non-overlapping sessions.

As a group:

0. Decide which session to consider first.
1. State the rule used to choose it.
2. Apply the rule to the candidate list.
3. Explain why choosing the earliest finishing compatible session is useful.

This is a separate mini-task. You do not need to implement it, but you must explain the greedy choice in your group notes.


### Stretch Challenges

Complete one or more of these challenges if you finish the core task early.

0.  Explain the Search
    -   Use a call to `print()` to display a short trace showing each event time and the attendance count after the events at that time are processed. Use the trace to explain how the best interval was selected.
0.  Report All Best Times
    -   If several intervals have the same maximum attendance, return every interval with that attendance rather than returning only the earliest one.
0.  Choose the Longest Best Time
    -   When several intervals tie for maximum attendance, choose the longest interval.  If several intervals still tie, choose the earliest one.
0.  Minimum Attendance Requirement
    -   Ask the user for a minimum number of attendees. Report the earliest interval that meets the requirement, or report that no suitable time exists.
0.  Predict Before You Run
    -   Replace `availability` with this larger set of intervals. Some intervals are intentionally duplicated:
        -   ```python
            availability = [
                (9, 11),
                (10, 14),
                (11, 13),
                (8, 12),
                (10, 14),
                (8, 12),
                (9, 11),
                (10, 14),
                (8, 12),
                (12, 15),
                (13, 16),
                (9, 12),
                (7, 9),
                (11, 13),
                (12, 15),
            ]
            ```
    -   Before running the program, predict the best interval, the maximum attendance, and the output selected when multiple intervals tie. Write down the reasoning behind your prediction.
    -   Then run the program and compare its output with your prediction.
    -   Do not decide that the program is correct merely because it produces a plausible answer. Verify the result by creating an event table by hand:
        * list every distinct event time in order
        * count how many intervals start and end at each time
        * update the attendance count using the half-open interval rule
        * identify every interval that reaches the maximum count
    -   Use the table to check both the attendance count and the tie-breaking rule.
    -   Explain how you know the program is correct, and identify any additional input you would use to test it further.


# Code Lab Challenge #1 - Binary Search with Library Books

In this challenge you will build a library catalog search that uses **binary search**.
The catalog is already sorted alphabetically by book title. Your program must find a
title quickly and report where a missing title belongs.

*Note: Students with deeper programming experience can try the stretch challenges in
Phase 4.*


### Program Requirements

0. Store the catalog as a list of book titles sorted in ascending alphabetical order.
1. Write a function named `binary_search_book` that accepts the catalog and a target title.
2. Use binary search. Do not scan the catalog from beginning to end.
3. If the target title is present, return its index.
4. If the target title is not present, return the index where it should be inserted
   to preserve alphabetical order.
5. Display a clear message for both found titles and missing titles.
6. To test the program, try searching for titles near the beginning, middle,
   and end of the catalog, as well as a title that is not present.


<details>
<summary><h3>library_search.py</h3></summary>

```python
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
```

</details>

Download [library_search.py](./library_search.py)


### Phase 0 - Predict

Create the file `challenge1.md` in your GitHub repo.

Work in a stable group with rotating roles: *driver*, *navigator*, *verifier*, and *reporter*.  You must take on a different role for each challenge. Note your role for this challenge in `challenge1.md`.

Before discussing with your group or running the program, predict the result for one
found title and one missing title. Record the expected `low`, `high`, and `middle`
values for at least one search in your `challenge1.md`.
**Do not run the program until every group member has recorded a prediction.**

Write answers to these questions in `challenge1.md`:

0.  What should the program report when the title is found?
0.  What should the program report when the title is missing?


### Phase 1 - Discuss

The *navigator* facilitates the discussion as team members compare their predictions.

The *reporter* notes any disagreements.


### Phase 2 - Implement

Under the direction of the *navigator*, the *driver* writes pseudocode in a code block
in `challenge1.md`. Surround it with Python fences, like this:

~~~
```python
# your code goes here
...
pass
```
~~~

Your pseudocode should explain how to:

0. Set the initial search range.
1. Choose the middle position.
2. Compare the middle title with the target title.
3. Discard the half that cannot contain the target.
4. Return either the matching index or the insertion position.

With the help of the *navigator*, the *driver* refines the pseudocode until it
approaches line-for-line equivalence with Python code. The *verifier* checks its
accuracy.


Then, the *driver* copies the pseudocode from `challenge1.md` into the starter code
file and comments it out. Under the guidance of the *navigator*, the *driver* replaces
each comment with runnable Python code until the program is complete.

### Phase 3 - Verify

Run the program with several titles. The *verifier* ensures that these cases are checked:

* the first title
* the last title
* a middle title
* missing before the first title
* missing between two titles
* missing after the last title

Create a shared boundary-case table showing the predicted result, program result, and
whether the case passed.


### Phase 4 - Explain

All members answer these debrief questions in their own `challenge1.md`:

* How did the search range change after each comparison?
* Why does the algorithm return the correct insertion position when the title is missing?
* What input would help you discover a boundary error in your program?
* Did your pseudocode line up with the code you wrote? If not, what changed?

The *reporter* prepares to share one boundary case and the evidence that your program
handled it correctly with the entire class.


### Stretch Challenges

Complete one or more of these challenges if you finish the core task early.

0.  First Matching Edition
    -   Create duplicate titles in the catalog (but preserve the sorted order). If the target title appears more than once, return the index of its **first** occurrence rather than an arbitrary matching index.
    -    Explain in a comment what the algorithm does after it finds a matching title.
1.  Explain the Search
    -   Create a second function that reports the titles examined during the search.
    -   For example, the function could return both the final index and a list of the titles checked at each middle position. Use that information to explain how binary search avoids checking every book.
2.  Search a Descending Catalog
    -   Create a version of the search that works with a catalog sorted from Z to A.
    -   Identify which comparisons or range updates must change. Test both a found title and an insertion position in the descending catalog.
3.  Number of Operations
    -   Count the number of comparisons used for each search. Consider how the number of comparisons changes as the catalog becomes larger.


# Code Lab Challenge #2 - Dijkstra's Algorithm by Hand

You are helping a delivery company find the shortest route through a network of
delivery hubs. Each hub is connected by roads with nonnegative distances.

Today you will use a projected graph generator to solve two different shortest-path
problems. You will first work through one problem as a class, then solve a more
challenging problem in a small group.

You will not write any code during the main activity. Your goal is to understand
the state changes and decisions that a Python implementation will need to perform.


### Algorithm Rules

For each problem:

0. Set the starting node's distance to `0`.
1. Set every other node's tentative distance to infinity.
2. Choose the unfinalized node with the smallest tentative distance.
3. Mark that node as finalized.
4. Check each of its neighbors.
5. Replace a neighbor's distance when the route through the current node is shorter.
6. Record the current node as the neighbor's previous node whenever its distance changes.
7. Continue until the destination is finalized or no reachable unfinalized nodes remain.

*n.b. Dijkstra's algorithm assumes that edge weights are nonnegative.*


### The Working Table

For every problem, maintain a table like this one:

| Node       | Tentative distance | Previous node | Finalized? |
|------------|-------------------:|---------------|------------|
| Start      |                  0 | N/A           | False      |
| Other node | infinity ∞         | N/A           | False      |

Use the `Previous node` column to reconstruct the final route by working backward
from the destination.


## Phase 0 - Predict

The instructor will display a randomly generated graph for the entire class.
This walkthrough prepares you for the shortest-route implementation challenge.

Create the file `challenge2.md` in your GitHub repo.

Before discussing with your group, predict the next finalized node and distance
updates individually. Write your own prediction in `challenge2.md`. The instructor will reveal or validate each step only after the class has committed to a prediction.

As a class, determine:

0. Which node should be finalized first?
0. Which node should be finalized next?

Before the instructor reveals each step, record your prediction in `challenge2.md`.  Represent the working table as best you can in Markdown.


## Phase 1 - Discuss

Work in a stable group with rotating roles: *driver*, *navigator*, *verifier*, and *reporter*.  You must take on a different role for each challenge. Note your role for this challenge in `challenge2.md`.

The instructor will now project a more difficult graph.  Your group must complete the following:

0. Fill in the tentative distance, previous node, and finalized status for every node.
1. Identify the order in which nodes are finalized.
2. Identify every distance that changes during the algorithm.
3. Report the shortest distance from the starting node to the destination.
4. Reconstruct the shortest route using the previous-node information.
5. Explain one decision where the algorithm chose between competing routes.
6. Explain why one node was finalized before another node.

If the destination is unreachable, report that clearly and explain how the algorithm determined that no route exists.

* The *driver* writes for the group.
* The *navigator* proposes the next algorithmic step and makes the final decision about what the driver writes.
* The *verifier* checks the navigator's thinking and proposes tests or counterexamples.
* The *reporter* records disagreements and prepares to represent the group.


## Phase 2 - Verify

The *verifier* checks the group's table against the projected graph and the generator's
validated result.

The group must verify:

0. The order in which your group finalized the nodes.
1. One important distance update.
2. The final shortest route and distance.
3. One place where your group had to correct or question its first idea.

The reporter records the group's final claim and the evidence supporting it.

## Phase 3 - Explain

The *reporter* will briefly present the group's reasoning to the class. Focus on one
important update, one decision the group had to resolve, and the final route.

**Do not read every row of the table aloud!** Focus on the decisions that show *how*
the algorithm works.


All members answer these debrief questions in their own `challenge2.md`:

*   Why is the first route discovered not necessarily the shortest route?
*   Why can a finalized node no longer receive a shorter distance?
*   What is the difference between a tentative distance and a finalized distance?
*   How did the previous-node column help you reconstruct the route?
*   What would happen if one road had a negative distance?
*   Connect the table to Python code
    -   After the walkthrough, identify the Python data structures an implementation would need.
    -   Write a short paragraph or pseudocode outline explaining how a loop in the Python program would correspond to the repeated rows in your working table.


# Code Lab Challenge #3 - Implement Dijkstra's algorithm to Find the Shortest Route

In this challenge you will turn your hand-traced Dijkstra's algorithm into Python
code. A campus shuttle system stores locations and road distances in a weighted
graph. Your program must find the shortest route between two locations.

You may use your completed distance table from the Dijkstra walkthrough as a guide.
The graph will contain nonnegative edge weights.

*Note: Students with deeper programming experience can try the stretch challenges in
Phase 4.*


### Program Requirements

0. Use the adjacency-list graph provided in the starter code.
0. Fill in the definition of the function named `find_shortest_route`.
0. Use Dijkstra's algorithm rather than trying every possible route.
0. Use the value returned by `float('inf')` to represent infinity.
0. Return the minimum total distance from the starting location to the destination.
0. Return the route as a list of location names in travel order.
0. Return `float('inf')` and an empty list when the destination cannot be reached.
0. Do not modify the graph while searching.
0. Assume all road distances are nonnegative.


<details>
<summary><h3>shortest_route.py</h3></summary>

```python
# shortest_route.py

class CampusMap:
    def __init__(self):
        self.graph = {}

    def add_location(self, location: str) -> None:
        if location not in self.graph:
            self.graph[location] = {}

    def add_path(self, first: str, second: str, distance: int) -> None:
        self.add_location(first)
        self.add_location(second)
        self.graph[first][second] = distance
        self.graph[second][first] = distance

    def find_shortest_route(
        self, start: str, destination: str
    ) -> tuple[int | float, list[str]]:
        """
        Return (distance, route) for the shortest route from start to destination.

        Return (float('inf'), []) if destination cannot be reached.
        """
        # YOUR CODE HERE
        pass  # Erase this line when you add your own code


ensign = CampusMap()

campus.add_path("Mathematics", "Admissions", 5)
campus.add_path("Library", "IT Offices", 6)
campus.add_path("Interior Design", "Computer Science", 4)
campus.add_path("Administration", "Admissions", 8)
campus.add_path("Business", "Outpost", 5)
campus.add_path("Computer Science", "Outpost", 3)
campus.add_path("Library", "Admissions", 1)
campus.add_path("Communications", "Mathematics", 2)
campus.add_path("Administration", "Mathematics", 3)
campus.add_path("Administration", "Interior Design", 2)
campus.add_path("Library", "Outpost", 2)
campus.add_path("Admissions", "Business", 4)
campus.add_path("Outpost", "Administration", 9)
campus.add_path("IT Offices", "Administration", 1)
campus.add_path("Mathematics", "Computer Science", 3)
campus.add_path("Business", "Library", 3)

distance, route = ensign.find_shortest_route("Business", "Computer Science")
print(f"Distance: {distance}")
print(f"Route: {' -> '.join(route)}")
```

</details>

Download [shortest_route.py](./shortest_route.py)


### Phase 0 - Predict

Create the file `challenge3.md` in your GitHub repo.

Work in a stable group with rotating roles: *driver*, *navigator*, *verifier*, and *reporter*.  You must take on a different role for each challenge. Note your role for this challenge in `challenge3.md`.

Before running the starter program with your group, write your individual prediction for the distance and route for the starter graph in `challenge3.md`. Connect each part of your hand-traced table to a Python data structure.
**Do not run the program until every group member has recorded a prediction.**

0. How will the program represent locations that have not been reached yet?
0. How will the program remember which locations are finalized?


### Phase 1 - Discuss

The *navigator* facilitates the discussion as team members compare their predictions.

The *reporter* notes any disagreements.


### Phase 2 - Implement

Under the direction of the *navigator*, the *driver* writes pseudocode in a code block
in `challenge3.md`. Surround it with Python fences, like this:

~~~
```python
# your code goes here
...
pass
```
~~~

Your pseudocode should explain how to:

0. Initialize the distance, previous-location, and finalized-location data.
1. Set the starting location's distance to zero.
2. Select the unfinalized location with the smallest known distance.
3. Update each neighboring location when a shorter route is found.
4. Stop when the destination is finalized or no reachable locations remain.
5. Reconstruct the route by following previous locations backward.

With the help of the *navigator*, the *driver* refines the pseudocode until it
approaches line-for-line equivalence with Python code. The *verifier* checks its
accuracy.


Then, the *driver* copies the pseudocode from `challenge3.md` into the starter code
file and comments it out. Under the guidance of the *navigator*, the *driver* replaces
each comment with runnable Python code until the program is complete.

### Phase 3 - Verify

Before running the program, the *verifier* hand-traces the starter graph using the
table from the Dijkstra walkthrough. Then compare the program's output with this
hand-traced result.

Try the function with:

* the starting location as the destination
* a destination that is directly connected
* a destination that requires several roads
* a route where the first route discovered is not the shortest route
* a location that does not exist in the map

Your group must keep a shared implementation record containing:

* the order in which locations were finalized
* one distance update
* the final route and distance
* the result for an unreachable destination

The *verifier* confirms that each test result matches the group's prediction or
records why the prediction was wrong.


### Phase 4 - Explain

All members answer these debrief questions in their own `challenge3.md`:

* Which part of the hand-traced table became the main loop in your program?
* Which data structure stores the tentative distances? Why is it appropriate?
* How does the previous-location data let you reconstruct the route?
* What invariant tells you that a finalized distance is correct?
* How did hand tracing help you find or prevent a coding error?

The *reporter* prepares to present one important distance update, the final route, and
one disagreement the group resolved to the entire class. Do not read every row of the
table aloud.


### Stretch Challenges

Complete one or more of these challenges if you finish the core task early.

0.  Return the Step-by-Step Distances
    -   Return or display the best known distance after each location is finalized. Use this trace to compare the program with the hand-traced table.
1.  Explain an Unreachable Destination
    -   Return a message explaining that no route exists when the destination cannot be reached. Make sure the program does not loop forever when the graph has disconnected parts.
2.  Add a Route Summary
    -   Display the route as named steps and calculate the distance of each individual road along the route. The individual distances should add up to the total distance.
3.  Analyze Scaling
    -   Write a short explanation of how the implementation's running time changes as the number of locations and roads increases. Identify one data structure or algorithmic change that could improve performance for a much larger graph.


# Code Lab Challenge #4 - Repair My Binary Search

Find and fix the bugs in this program.

The program searches a sorted library catalog. If it finds the requested title, it
returns that title's index. If the title is missing, it returns the index where the
title should be inserted to preserve alphabetical order.

The program must use binary search. Do not replace it with a linear scan or a built-in
search function.


<details>
<summary><h3>broken_search.py</h3></summary>

```python
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
describe_result("Hacker's Delight")
describe_result("Operating Systems")
```

</details>

Download [broken_search.py](./broken_search.py)


### Program Requirements

Repair the program so that it:

0. Uses binary search.
1. Returns the correct index for a title that is present.
2. Returns the correct insertion index for a title that is missing.
3. Handles a title that belongs before the first item.
4. Handles a title that belongs after the last item.
5. Handles an empty catalog without crashing.
6. Always makes progress toward ending the search.


### Phase 0 - Predict

Create the file `challenge4.md` in your GitHub repo.

Work in a stable group with rotating roles: *driver*, *navigator*, *verifier*, and *reporter*.  You must take on a different role for each challenge. Note your role for this challenge in `challenge4.md`.

Run only the designated diagnostic inputs before identifying the bugs. Each student
must predict what will happen for at least one input.
**Do not run the program until every group member has recorded a prediction.**

Write answers to these questions in `challenge4.md`:

0.  What do `low` and `high` represent?
0.  What part of the search is represented by the current range?
0.  What should the final value of `low` represent when the target is missing?

Trace the program by hand for at least one title that is present and one title that is
missing. Record the values of `low`, `high`, and `middle` after each iteration.


### Phase 1 - Discuss

The *navigator* facilitates the discussion as team members compare their predictions
and suspected bugs. The *reporter* notes disagreements.


### Phase 2 - Repair

The *navigator's* goal is to **make the smallest changes needed to repair the program.**

The *verifier* ensures that the *navigator* keeps the overall binary-search structure. Add short comments explaining any changes to the loop condition or range updates.

The *driver* records each repair in this format:

```text
Bug:
Evidence:
Fix:
Verification:
```


### Phase 3 - Verify

The *verifier* runs the program with a variety of inputs, and confirms that it handles:

* the first title
* the last title
* a title in the middle
* a missing title before the first title
* a missing title between two titles
* a missing title after the last title
* an empty catalog

Also test a one-title catalog. For each case, record the expected insertion position
before running the program.

Exchange one test input with another group. The *reporter* explains why your input should expose a
boundary or progress bug, then compare the other group's result with your prediction.


### Phase 4 - Explain

All members answer these debrief questions in `challenge4.md`:

* Which bug caused the program to stop too early?
* Which bug could cause the search range to stop shrinking?
* Why is returning `low` useful when the target is missing?
* What invariant is true about the possible location of the target during the search?
* How did hand tracing help you locate the bugs?

The *reporter* prepares to share one bug, the evidence that exposed it, and the
verification that showed the repair worked.


### Stretch Challenges

Complete one or more of these challenges if you finish early.

0.  First Matching Edition
    -   Allow duplicate titles in the catalog. Return the index of the first occurrence of the target title.
1.  Explain the Search
    -   Return or display the values of `low`, `high`, and `middle` from every iteration.  Use the trace to explain how the search range shrinks.
2.  Stretch 3 - Search a Descending Catalog
    -   Repair or adapt the function so that it works with a catalog sorted from Z to A.
3.  Count Comparisons
    -   Count how many title comparisons the function makes. Compare the count for catalogs with different sizes and explain the pattern you observe.



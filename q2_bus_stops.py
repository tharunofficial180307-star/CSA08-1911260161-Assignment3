"""Q2: City Bus-Stop Map – Tuples, Mutability, Copying, and Sparse Grid."""
import copy
import sys

rows, cols = 3, 4
bad = [[0] * cols] * rows          # every row is the SAME list object
bad[0][1] = 7
# TODO 1 Completed: Create a rows x cols grid of zeros using a list comprehension
good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7

stops = {(13.0827, 80.2707): "Chennai Central", (13.0418, 80.2341): "T. Nagar"}

if __name__ == "__main__":
    print("bad :", bad)
    print("good:", good)
    print(bad[0] is bad[1], good[0] is good[1])
    print(stops[(13.0418, 80.2341)])

    try:
        _ = {[13.0418, 80.2341]: "Error"}
    except TypeError as err:
        print("List as dict key error:", err)

    shallow = copy.copy(good)
    deep = copy.deepcopy(good)
    good[1][2] = 99
    print("Shallow reflects inner change:", shallow[1][2] == 99, "| Deep isolated:", deep[1][2] == 0)

    lst = list(range(100_000))
    tup = tuple(lst)
    print(f"Memory (100k) -> list: {sys.getsizeof(lst)} bytes, tuple: {sys.getsizeof(tup)} bytes")

"""Q4: Elective Registration Clash Detection – Set Operators, Methods, and Benchmarks."""
import time

ai_elective = {"192311001", "192311004", "192311007", "192311009"}
iot_elective = {"192311002", "192311004", "192311009", "192311010"}
all_students = {f"1923110{i:02d}" for i in range(1, 11)}

# TODO 1 Completed: Set operators
both = ai_elective & iot_elective
exactly_one = ai_elective ^ iot_elective
neither = all_students - (ai_elective | iot_elective)

if __name__ == "__main__":
    print("clash      :", sorted(both))
    print("exactly one:", sorted(exactly_one))
    print("neither    :", sorted(neither))

    assert both == ai_elective.intersection(iot_elective)
    assert exactly_one == ai_elective.symmetric_difference(iot_elective)
    assert neither == all_students.difference(ai_elective.union(iot_elective))

    for n in (10_000, 100_000, 1_000_000):
        lst = list(range(n))
        st = set(lst)
        target = n - 1
        t0 = time.perf_counter(); _ = target in lst; t_list = (time.perf_counter() - t0) * 1e6
        t0 = time.perf_counter(); _ = target in st; t_set = (time.perf_counter() - t0) * 1e6
        print(f"n={n:7d} | list lookup: {t_list:8.2f} us | set lookup: {t_set:6.2f} us")

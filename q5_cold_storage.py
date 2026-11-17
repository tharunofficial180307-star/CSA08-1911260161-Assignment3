"""Q5: Cold-Storage Temperature Monitor – Loops, Comprehensions, Map/Filter, Generators."""
import random
import sys
import time

def clean_loop(readings):
    valid_c, valid_f = [], []
    for c in readings:
        if -50.0 <= c <= 50.0:
            valid_c.append(c)
            valid_f.append(round(c * 9 / 5 + 32, 2))
    return valid_c, valid_f

def clean_comp(readings):
    valid_c = [c for c in readings if -50.0 <= c <= 50.0]
    valid_f = [round(c * 9 / 5 + 32, 2) for c in readings if -50.0 <= c <= 50.0]
    return valid_c, valid_f

def clean_map_filter(readings):
    valid_c = list(filter(lambda c: -50.0 <= c <= 50.0, readings))
    valid_f = list(map(lambda c: round(c * 9 / 5 + 32, 2), valid_c))
    return valid_c, valid_f

if __name__ == "__main__":
    rng = random.Random(2026)
    data = [rng.choice([-99.0, 99.0, round(rng.uniform(1.0, 10.0), 1)]) for _ in range(100_000)]
    alarms = [idx for idx, c in enumerate(data) if -50.0 <= c <= 50.0 and not (2.0 <= c <= 8.0)]
    c1, f1 = clean_loop(data)
    c2, f2 = clean_comp(data)
    c3, f3 = clean_map_filter(data)
    assert c1 == c2 == c3 and f1 == f2 == f3
    gen = (c for c in data if -50.0 <= c <= 50.0)
    print(f"Valid count: {len(c1)} | Alarm minutes: {len(alarms)}")
    print(f"Memory -> List: {sys.getsizeof(c2)} bytes | Generator: {sys.getsizeof(gen)} bytes")

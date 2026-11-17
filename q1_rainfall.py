"""Q1: Daily Rainfall Records – Slicing, Naive vs Running-Sum Moving Average, and Deque."""
from collections import deque
import random
import time

def moving_avg_naive(readings, k=7):
    if len(readings) < k:
        return []
    return [round(sum(readings[i:i + k]) / k, 2) for i in range(len(readings) - k + 1)]

def moving_avg_running(readings, k=7):
    n = len(readings)
    if n < k:
        return []
    window_sum = sum(readings[:k])
    avgs = [round(window_sum / k, 2)]
    for i in range(k, n):
        window_sum += readings[i] - readings[i - k]
        avgs.append(round(window_sum / k, 2))
    return avgs

def moving_avg_deque(readings, k=7):
    if len(readings) < k:
        return []
    win = deque(maxlen=k)
    avgs = []
    for val in readings:
        win.append(val)
        if len(win) == k:
            avgs.append(round(sum(win) / k, 2))
    return avgs

if __name__ == "__main__":
    rng = random.Random(2026)
    year = [rng.choice([0.0, 0.0, round(rng.uniform(1.0, 45.0), 1)]) for _ in range(365)]
    weekly = [round(sum(year[i:i + 7]), 1) for i in range(0, 364, 7)]
    dry_days = [i for i, v in enumerate(year) if v == 0.0]
    print(f"Dry days count: {len(dry_days)} | Max week: {max(weekly)} mm | Min week: {min(weekly)} mm")

    for n in (365, 36500, 365000):
        data = [rng.uniform(0, 50) for _ in range(n)]
        t0 = time.perf_counter(); r1 = moving_avg_naive(data); t_naive = (time.perf_counter() - t0) * 1000
        t0 = time.perf_counter(); r2 = moving_avg_running(data); t_run = (time.perf_counter() - t0) * 1000
        assert r1 == r2
        print(f"n={n:6d} | Naive: {t_naive:7.2f} ms | Running-sum: {t_run:6.2f} ms")

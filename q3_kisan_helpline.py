"""Q3: Farmer Helpline Complaint Analysis – Dictionaries, Grouping, and Counter."""
from collections import Counter
import re

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}

def frequencies(texts, stop):
    # TODO 1 Completed: Return a dictionary word -> count for words not in stop
    counts = {}
    for text in texts:
        cleaned = re.sub(r"[^a-z0-9\s]", "", text.lower())
        for word in cleaned.split():
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    # TODO 2 Completed: Return k most frequent (word, count) pairs, count desc, word asc
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:k]

def group_by_district(records):
    grouped = {}
    for district, complaint in records:
        grouped.setdefault(district, []).append(complaint)
    return grouped

if __name__ == "__main__":
    print(top(frequencies(calls, STOP), 3))
    print("Grouped:", group_by_district([("Thanjavur", "Water shortage"), ("Salem", "Pest attack"), ("Thanjavur", "Seeds late")]))

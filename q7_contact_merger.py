"""Q7: Merging Phone Contacts from First Principles – O(n) Hash Grouping."""
import re
import time

def normalise_phone(raw):
    digits = re.sub(r"\D", "", raw or "")
    return digits[-10:] if len(digits) >= 10 else digits

def normalise_name(raw):
    cleaned = re.sub(r"\b(dr|mr|mrs|ms|prof)\.?\s*", "", (raw or "").strip().lower())
    return " ".join(w.capitalize() for w in cleaned.split())

def merge_contacts(records):
    merged = {}
    for name, phone, email in records:
        key = normalise_phone(phone)
        if not key:
            continue
        if key not in merged:
            merged[key] = {"name": normalise_name(name), "phones": set(), "emails": set()}
        else:
            cand = normalise_name(name)
            if len(cand) > len(merged[key]["name"]):
                merged[key]["name"] = cand
        merged[key]["phones"].add(phone.strip())
        if email and email.strip():
            merged[key]["emails"].add(email.strip().lower())
    return merged

if __name__ == "__main__":
    sample = [
        ("Dr. Ravi", "+91 98400 12345", "ravi@mail.com"),
        ("ravi kumar", "9840012345", "RAVI@MAIL.COM"),
        ("Ravi Kumar", "9123456789", "other_ravi@mail.com"),
    ]
    res = merge_contacts(sample)
    for k, v in res.items():
        print(k, "->", v)

    big = [(f"User {i%20000}", f"+91 98400 {i%20000:05d}", f"u{i%20000}@ex.com") for i in range(100_000)]
    t0 = time.perf_counter()
    m_big = merge_contacts(big)
    print(f"Merged 100,000 contacts into {len(m_big)} unique entries in {(time.perf_counter()-t0)*1000:.2f} ms")

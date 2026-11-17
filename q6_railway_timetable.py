"""Q6: Railway Enquiry Counter – Nested Dictionary vs Inverted Station Index."""

TIMETABLE = {
    "12637": {"name": "Pandian Exp", "stops": [("MS", "21:20", "21:40"), ("TPJ", "02:15", "02:20"), ("MDU", "04:20", "04:30")], "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}},
    "12675": {"name": "Kovai Exp", "stops": [("MAS", "06:00", "06:10"), ("KPD", "07:53", "07:55"), ("CBE", "13:40", "13:50")], "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}},
    "12607": {"name": "Lalbagh Exp", "stops": [("MAS", "15:25", "15:35"), ("KPD", "17:18", "17:20"), ("SBC", "21:35", "21:45")], "days": {"Mon", "Wed", "Fri", "Sun"}},
    "12633": {"name": "Kanyakumari Exp", "stops": [("MS", "17:10", "17:20"), ("TPJ", "22:10", "22:15"), ("CAPE", "05:35", "05:45")], "days": {"Tue", "Thu", "Sat"}},
    "12623": {"name": "Trivandrum Mail", "stops": [("MAS", "19:35", "19:45"), ("KPD", "21:28", "21:30"), ("TVC", "11:45", "11:55")], "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}},
}

def build_station_index(tt):
    index = {}
    for tno, info in tt.items():
        for stn, arr, dep in info["stops"]:
            index.setdefault(stn, []).append((tno, info["name"], arr, dep, info["days"]))
    return index

def query_indexed(index, station, day):
    matches = [
        (tno, name, dep)
        for tno, name, arr, dep, days in index.get(station, [])
        if day in days
    ]
    return sorted(matches, key=lambda x: x[2])

if __name__ == "__main__":
    print("3rd station departure of 12637:", TIMETABLE["12637"]["stops"][2][2])
    idx = build_station_index(TIMETABLE)
    print("Trains at KPD on Mon:", query_indexed(idx, "KPD", "Mon"))

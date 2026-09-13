def calculate_part_a(events, total_hours=720):
    total_downtime = sum(event["duration"] for event in events)
    total_uptime = total_hours - total_downtime
    failure_count = len(events)
    
    availability = (total_uptime / total_hours) * 100
    mttf = total_uptime / failure_count
    mttr = total_downtime / failure_count
    mtbf = mttf + mttr
    
    return {
        "total_downtime": total_downtime,
        "total_uptime": total_uptime,
        "availability": availability,
        "mttf": mttf,
        "mttr": mttr,
        "mtbf": mtbf
    }

if __name__ == "__main__":
    # Sample dataset test
    raw_events = [
        {"duration": 2}, {"duration": 4}, {"duration": 1},
        {"duration": 2}, {"duration": 4}, {"duration": 1},
        {"duration": 2}, {"duration": 2}, {"duration": 5},
        {"duration": 2}, {"duration": 1}, {"duration": 1}
    ]
    results = calculate_part_a(raw_events)
    print("Part A Results:", results)
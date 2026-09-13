from part_a import calculate_part_a
from part_b import calculate_part_b
from part_c import calculate_part_c
from part_d import calculate_part_d

EVENTS = [
    {"event": 1, "component": "Application Server A", "duration": 2},
    {"event": 2, "component": "Primary Database", "duration": 4},
    {"event": 3, "component": "Campus Network", "duration": 1},
    {"event": 4, "component": "Application Server B", "duration": 2},
    {"event": 5, "component": "Primary Database", "duration": 4},
    {"event": 6, "component": "Load Balancer", "duration": 1},
    {"event": 7, "component": "Application Server A", "duration": 2},
    {"event": 8, "component": "Campus Network", "duration": 2},
    {"event": 9, "component": "Primary Database", "duration": 5},
    {"event": 10, "component": "Application Server B", "duration": 2},
    {"event": 11, "component": "Application Server A", "duration": 1},
    {"event": 12, "component": "Load Balancer", "duration": 1},
]

TOTAL_OPERATING_HOURS = 720

def main():
    part_a = calculate_part_a(EVENTS, TOTAL_OPERATING_HOURS)
    part_b = calculate_part_b()
    part_c = calculate_part_c()
    part_d = calculate_part_d()

    print("=" * 60)
    print("AITU STUDENT PORTAL RELIABILITY ANALYSIS")
    print("=" * 60)

    print("\n[PART A: RELIABILITY METRICS]")
    print(f"Total Downtime : {part_a['total_downtime']} hours")
    print(f"Total Uptime   : {part_a['total_uptime']} hours")
    print(f"Availability   : {part_a['availability']:.2f}%")
    print(f"MTTF           : {part_a['mttf']:.2f} hours")
    print(f"MTTR           : {part_a['mttr']:.2f} hours")
    print(f"MTBF           : {part_a['mtbf']:.2f} hours")

    print("\n[PART B: SUBSYSTEM RELIABILITY]")
    print(f"App Subsystem  : {part_b['r_app_subsystem']:.4f}")
    print(f"DB Subsystem   : {part_b['r_db_subsystem']:.4f}")
    print(f"Overall System : {part_b['r_overall']:.4f} ({part_b['r_overall'] * 100:.2f}%)")

    print("\n[PART C: FMEA TOP 3 RPN RISKS]")
    for i, item in enumerate(part_c[:3], 1):
        print(f"{i}. {item['component']} -> RPN: {item['RPN']} (S:{item['S']}, O:{item['O']}, D:{item['D']})")

    print("\n[PART D: FAULT TREE ANALYSIS (TOP EVENT)]")
    print(f"App Subsystem Unavailability (AND Gate) : {part_d['q_app_subsystem']:.6f}")
    print(f"DB Subsystem Unavailability (AND Gate)  : {part_d['q_db_subsystem']:.6f}")
    print(f"Top Event Outage Risk (OR Gate)        : {part_d['q_top_event']:.6f}")
    print("=" * 60)

if __name__ == "__main__":
    main()
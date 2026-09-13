from part_a import calculate_part_a
from part_b import calculate_part_b

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
    
    print("=" * 55)
    print("AITU STUDENT PORTAL RELIABILITY ANALYSIS")
    print("=" * 55)
    
    print("\n[PART A: RELIABILITY METRICS]")
    print(f"Total Operating Time : {TOTAL_OPERATING_HOURS} hours")
    print(f"Total Downtime       : {part_a['total_downtime']} hours")
    print(f"Total Uptime         : {part_a['total_uptime']} hours")
    print(f"Availability         : {part_a['availability']:.2f}%")
    print(f"MTTF                 : {part_a['mttf']:.2f} hours")
    print(f"MTTR                 : {part_a['mttr']:.2f} hours")
    print(f"MTBF                 : {part_a['mtbf']:.2f} hours")
    
    print("\n[PART B: SUBSYSTEM & OVERALL RELIABILITY]")
    print(f"Load Balancer        : {part_b['r_lb']:.4f}")
    print(f"App Subsystem (OR)   : {part_b['r_app_subsystem']:.4f}")
    print(f"DB Subsystem (OR)    : {part_b['r_db_subsystem']:.4f}")
    print(f"Campus Network       : {part_b['r_net']:.4f}")
    print(f"Overall Reliability  : {part_b['r_overall']:.4f} ({part_b['r_overall'] * 100:.2f}%)")
    print("=" * 55)

if __name__ == "__main__":
    main()
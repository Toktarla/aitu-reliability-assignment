def calculate_part_c():
    fmea_data = [
        {
            "component": "Primary Database",
            "failure_mode": "Data corruption / disk failure",
            "S": 9, "O": 6, "D": 5,
            "mitigation": "Automated failover to Standby DB and real-time replication"
        },
        {
            "component": "Standby Database",
            "failure_mode": "Sync delay / failover failure",
            "S": 7, "O": 3, "D": 6,
            "mitigation": "Frequent replication checks and automated health ping"
        },
        {
            "component": "Load Balancer",
            "failure_mode": "Hardware crash or config loss",
            "S": 10, "O": 3, "D": 4,
            "mitigation": "Add active-passive secondary Load Balancer with auto failover"
        },
        {
            "component": "Campus Network",
            "failure_mode": "Router failure / fiber break",
            "S": 8, "O": 3, "D": 4,
            "mitigation": "Backup secondary ISP line and redundant core router"
        },
        {
            "component": "Application A",
            "failure_mode": "Memory leak / process freeze",
            "S": 5, "O": 5, "D": 3,
            "mitigation": "Set auto-restart scripts and memory monitoring"
        },
        {
            "component": "Application B",
            "failure_mode": "Crash under high load",
            "S": 5, "O": 4, "D": 3,
            "mitigation": "Implement auto-scaling and load testing before semester"
        }
    ]

    # Calculate RPN = S * O * D for each component
    for item in fmea_data:
        item["RPN"] = item["S"] * item["O"] * item["D"]

    sorted_fmea = sorted(fmea_data, key=lambda x: x["RPN"], reverse=True)
    return sorted_fmea

if __name__ == "__main__":
    results = calculate_part_c()
    print("Part C FMEA RPN Rankings:")
    for item in results:
        print(f"- {item['component']} ({item['failure_mode']}): RPN = {item['RPN']}")
def calculate_part_d(r_lb=0.995, r_app_a=0.970, r_app_b=0.970, r_pri_db=0.980, r_stb_db=0.990, r_net=0.995):
    # Convert component reliability (R) to unavailability (Q = 1 - R)
    q_lb = 1 - r_lb
    q_app_a = 1 - r_app_a
    q_app_b = 1 - r_app_b
    q_pri_db = 1 - r_pri_db
    q_stb_db = 1 - r_stb_db
    q_net = 1 - r_net

    # Subsystem Unavailability using AND Gate logic: Q_sub = Q_1 * Q_2
    q_app_subsystem = q_app_a * q_app_b
    q_db_subsystem = q_pri_db * q_stb_db

    # Top Event Unavailability using OR Gate logic: Q_top = 1 - (1 - Q_1)(1 - Q_2)...
    r_top_system = (1 - q_lb) * (1 - q_app_subsystem) * (1 - q_db_subsystem) * (1 - q_net)
    q_top_event = 1 - r_top_system

    return {
        "q_app_subsystem": q_app_subsystem,
        "q_db_subsystem": q_db_subsystem,
        "q_top_event": q_top_event,
        "top_event_availability": r_top_system * 100
    }

if __name__ == "__main__":
    results = calculate_part_d()
    print("Part D FTA Calculations:")
    print(f"App Subsystem Failure Probability (AND Gate) : {results['q_app_subsystem']:.6f}")
    print(f"DB Subsystem Failure Probability (AND Gate)  : {results['q_db_subsystem']:.6f}")
    print(f"Top Event Outage Probability (OR Gate)       : {results['q_top_event']:.6f}")
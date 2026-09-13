def calculate_part_b(r_lb=0.995, r_app_a=0.970, r_app_b=0.970, r_pri_db=0.980, r_stb_db=0.990, r_net=0.995):
    r_app_subsystem = 1 - (1 - r_app_a) * (1 - r_app_b)
    r_db_subsystem = 1 - (1 - r_pri_db) * (1 - r_stb_db)
    
    # Overall system in series
    r_overall = r_lb * r_app_subsystem * r_db_subsystem * r_net
    
    return {
        "r_lb": r_lb,
        "r_app_subsystem": r_app_subsystem,
        "r_db_subsystem": r_db_subsystem,
        "r_net": r_net,
        "r_overall": r_overall
    }

if __name__ == "__main__":
    results = calculate_part_b()
    print("Part B Results:", results)
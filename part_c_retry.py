from data import TRANSACTIONS, simulate_attempt

def run_retry_processor():
    print("=== PART C: RETRY MECHANISM & STEP LOG ===")
    
    step = 1
    attempt_logs = []
    
    print(f"{'Step':<6} | {'Tx ID':<6} | {'Attempt':<15} | {'Failure':<10} | {'Action':<15} | {'Result':<8}")
    print("-" * 75)
    
    for tx in TRANSACTIONS:
        for attempt in range(3): # 0: Initial, 1: Retry 1, 2: Retry 2
            res = simulate_attempt(tx, attempt)
            
            attempt_label = "Initial Attempt" if attempt == 0 else f"Retry {attempt}"
            
            if res == "Success":
                action = "Execute"
            else:
                action = "Escalate/Retry" if tx["fault"] != "Database" else "Abort"
            
            failure_type = tx["fault"] if res == "Fail" else "None"
            step_str = f"S{step:02d}"
            
            print(f"{step_str:<6} | {tx['id']:<6} | {attempt_label:<15} | {failure_type:<10} | {action:<15} | {res:<8}")
            
            attempt_logs.append({
                "step": step_str, "tx": tx['id'], "attempt": attempt_label,
                "failure": failure_type, "action": action, "result": res
            })
            
            step += 1
            if res == "Success":
                break
                
    return attempt_logs

if __name__ == "__main__":
    run_retry_processor()
from data import TRANSACTIONS, simulate_attempt, NetworkError

def run_baseline():
    print("PART A: BASELINE PROCESSOR")
    
    attempted = 0
    successful = 0
    processed_amt = 0
    
    for tx in TRANSACTIONS:
        attempted += 1
        print(f"Processing {tx['id']} ({tx['amount']} KZT)...")
        
        result = simulate_attempt(tx, attempt_number=0)
        
        if result == "Fail":
            print(f"  [CRASH] Unhandled {tx['fault']} fault on {tx['id']}! Processor stopped.")
            break
            
        successful += 1
        processed_amt += tx["amount"]
        print(f"  [SUCCESS] {tx['id']} completed.")

    total_count = len(TRANSACTIONS)
    total_amt = sum(t["amount"] for t in TRANSACTIONS)
    
    print("\n--- BASELINE METRICS ---")
    print(f"Transactions Attempted: {attempted}")
    print(f"Successful Transactions: {successful}")
    print(f"Transactions Lost: {total_count - successful}")
    print(f"Processed Amount: {processed_amt:,} KZT")
    print(f"Lost Amount: {total_amt - processed_amt:,} KZT")

if __name__ == "__main__":
    run_baseline()
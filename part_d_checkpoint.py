from data import TRANSACTIONS, simulate_attempt

def run_checkpoint_processor():
    print("=== PART D: CHECKPOINT & ROLLBACK PROCESSOR ===")
    
    successful_txs = []
    checkpoints = []
    total_processed_amt = 0
    
    for tx in TRANSACTIONS:
        tx_success = False
        
        for attempt in range(3):
            res = simulate_attempt(tx, attempt)
            
            if res == "Success":
                tx_success = True
                successful_txs.append(tx["id"])
                total_processed_amt += tx["amount"]
                print(f"[SUCCESS] {tx['id']} ({tx['amount']} KZT)")
                
                if len(successful_txs) % 5 == 0:
                    cp_num = len(successful_txs) // 5
                    cp_data = {
                        "checkpoint": f"CP{cp_num}",
                        "successful_count": len(successful_txs),
                        "total_amount": total_processed_amt,
                        "state_saved": list(successful_txs)
                    }
                    checkpoints.append(cp_data)
                    print(f"[CHECKPOINT CP{cp_num} CREATED] Saved {len(successful_txs)} txs, Total: {total_processed_amt:,} KZT")
                break
                
        if not tx_success:
            print(f"[FAIL/ROLLBACK] {tx['id']} failed permanently after retries (Fault: {tx['fault']}).")
            if checkpoints:
                last_cp = checkpoints[-1]
                print(f"  ==> Rolling back state to {last_cp['checkpoint']} (Valid Total: {last_cp['total_amount']:,} KZT)")
            else:
                print("  ==> Rolling back state to initial zero balance.")

    print("\n-------- FINAL SAVED CHECKPOINTS --------")
    for cp in checkpoints:
        print(f"{cp['checkpoint']}: {cp['successful_count']} Txs | Amount: {cp['total_amount']:,} KZT | State: {cp['state_saved']}")

if __name__ == "__main__":
    run_checkpoint_processor()
import logging
from data import TRANSACTIONS, simulate_attempt, NetworkError, TimeoutError, DatabaseError

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run_exception_handling():
    print("=== PART B: EXCEPTION HANDLING PROCESSOR ===")
    
    for tx in TRANSACTIONS:
        try:
            res = simulate_attempt(tx, attempt_number=0)
            if res == "Fail":
                if tx["fault"] == "Network":
                    raise NetworkError(f"Network glitch on {tx['id']}")
                elif tx["fault"] == "Timeout":
                    raise TimeoutError(f"Gateway timeout on {tx['id']}")
                elif tx["fault"] == "Database":
                    raise DatabaseError(f"DB lock on {tx['id']}")
            
            logging.info(f"Transaction {tx['id']} processed successfully.")
            
        except NetworkError as e:
            logging.warning(f"Caught Exception [{type(e).__name__}] on {tx['id']}. Recovery: Flagged for Retry 1.")
        except TimeoutError as e:
            logging.warning(f"Caught Exception [{type(e).__name__}] on {tx['id']}. Recovery: Flagged for Retry 2.")
        except DatabaseError as e:
            logging.error(f"Caught Exception [{type(e).__name__}] on {tx['id']}. Recovery: Direct to Abort/Rollback.")

if __name__ == "__main__":
    run_exception_handling()
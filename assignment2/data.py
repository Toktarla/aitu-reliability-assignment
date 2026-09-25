TRANSACTIONS = [
    {"id": "T001", "amount": 12000, "fault": "None"},
    {"id": "T002", "amount": 25000, "fault": "Network"},
    {"id": "T003", "amount": 8000,  "fault": "None"},
    {"id": "T004", "amount": 45000, "fault": "Timeout"},
    {"id": "T005", "amount": 13000, "fault": "None"},
    {"id": "T006", "amount": 70000, "fault": "Database"},
    {"id": "T007", "amount": 9000,  "fault": "None"},
    {"id": "T008", "amount": 31000, "fault": "Network"},
    {"id": "T009", "amount": 15000, "fault": "None"},
    {"id": "T010", "amount": 50000, "fault": "Timeout"},
    {"id": "T011", "amount": 6000,  "fault": "None"},
    {"id": "T012", "amount": 80000, "fault": "Database"},
    {"id": "T013", "amount": 11000, "fault": "None"},
    {"id": "T014", "amount": 22000, "fault": "None"},
    {"id": "T015", "amount": 40000, "fault": "Network"},
]

class PaymentProcessingError(Exception): pass
class NetworkError(PaymentProcessingError): pass
class TimeoutError(PaymentProcessingError): pass
class DatabaseError(PaymentProcessingError): pass

def simulate_attempt(tx: dict, attempt_number: int) -> str:
    fault = tx["fault"]
    
    if fault == "None":
        return "Success"
    elif fault == "Network":
        return "Success" if attempt_number >= 1 else "Fail"
    elif fault == "Timeout":
        return "Success" if attempt_number >= 2 else "Fail"
    elif fault == "Database":
        return "Fail"
    
    return "Fail"
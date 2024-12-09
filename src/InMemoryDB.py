class InMemoryDB:
    def __init__(self):
        self.main = {}
        self.transactions = None
        self.in_transaction = False
    
    def get(self, key):
        return self.main.get(key)
    
    def put(self, key, val):
        if not self.in_transaction:
            raise Exception("Transaction not in progress.")
        self.transactions[key] = val

    def begin_transaction(self) :
        if self.in_transaction:
           raise Exception("Transaction already in progress.") 
        self.transactions = {}
        self.in_transaction = True
    
    def commit(self): 
        if not self.in_transaction:
            raise Exception("Transaction not in progress.")
        for key, value in self.transactions.items():
            self.main[key] = value
        self.transactions = None
        self.in_transaction = False

    def rollback(self): 
        if not self.in_transaction:
            raise Exception("Transaction not in progress.")
        self.transactions = None
        self.in_transaction = False 
    
db = InMemoryDB()

print(db.get("A"))

try:
    db.put("A", 5)
except Exception as e:
    print(f"Error: {e}")

db.begin_transaction()

db.put("A", 5)

print(db.get("A"))

db.put("A", 6)

db.commit()

print(db.get("A"))

try:
    db.commit()
except Exception as e:
    print(f"Error: {e}")

try:
    db.rollback()
except Exception as e:
    print(f"Error: {e}")

print(db.get("B"))

db.begin_transaction()

db.put("B", 10)

db.rollback()

print(db.get("B"))
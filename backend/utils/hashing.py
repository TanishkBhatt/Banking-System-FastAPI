import hashlib

def hash_pin(pin: str) -> str:
    return hashlib.sha256(pin.encode()).hexdigest()

def verify(stored_hash: str, entered_pin: str) -> bool:
    return stored_hash == hash_pin(entered_pin) 
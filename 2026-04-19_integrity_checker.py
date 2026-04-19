import hashlib

def get_hash(filename):
    """Generates a SHA-256 hash for a file."""
    try:
        with open(filename, "rb") as f:
            bytes = f.read() # Read the entire file
            return hashlib.sha256(bytes).hexdigest()
    except FileNotFoundError:
        return None

# 1. The filename we want to watch
target_file = "important_data.txt"

# 2. Get the current hash
current_status = get_hash(target_file)

# 3. Compare (In a real scenario, you'd compare this to a saved string)
baseline_hash = "paste_your_original_hash_here"

if current_status == baseline_hash:
    print("File is safe. No changes detected.")
else:
    print("ALERT: File has been modified or tampered with!")
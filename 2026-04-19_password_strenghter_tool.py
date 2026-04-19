import re
import math

def evaluate_password(password):
    # Criteria definitions
    length = len(password)
    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<> \-_]", password)

    # Calculate Character Pool Size (R)
    pool_size = 0
    if has_lower: pool_size += 26
    if has_upper: pool_size += 26
    if has_digit: pool_size += 10
    if has_special: pool_size += 32  # Standard special char count

    if pool_size == 0 or length == 0:
        return 0, "Non-existent"

    # Entropy Calculation: L * log2(R)
    entropy = length * math.log2(pool_size)

    # Determine Strength Label
    if entropy < 40:
        strength = "Very Weak (Easily brute-forced)"
    elif entropy < 60:
        strength = "Weak (Risky)"
    elif entropy < 80:
        strength = "Moderate (Good for basic accounts)"
    elif entropy < 100:
        strength = "Strong (Secure)"
    else:
        strength = "Very Strong (Excellent)"

    return round(entropy, 2), strength

# User Interface
if __name__ == "__main__":
    print("--- Password Entropy Tool ---")
    user_input = input("Enter a password to test: ")
    
    score, label = evaluate_password(user_input)
    
    print(f"\nResults for: {user_input}")
    print(f"Entropy Score: {score} bits")
    print(f"Security Rating: {label}")
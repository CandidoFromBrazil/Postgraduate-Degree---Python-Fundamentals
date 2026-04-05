import random

print("--- D20 Roller ---")
print("Press Enter to roll, or type 'q' to quit.")

while True:
    user_input = input("> ").lower()
    
    if user_input == 'q':
        break

    roll = random.randint(1, 20)
    print(f"🎲 Result: {roll}")

print("Thanks for playing!")
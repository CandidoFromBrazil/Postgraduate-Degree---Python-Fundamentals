import secrets
import string

def generate_password(length=12):
    """Generates a secure random password."""
    # Define the character set: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by picking random characters securely
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

# Example usage: Generate a 16-character password
new_password = generate_password(16)
print(f"Your secure password is: {new_password}")

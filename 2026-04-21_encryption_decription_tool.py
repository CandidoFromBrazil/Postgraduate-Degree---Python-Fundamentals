from cryptography.fernet import Fernet # Make sure to install the 'cryptography' library if you haven't already:

# 1. GENERATE AND SAVE A KEY (Do this once)
def generate_key():
    key = Fernet.generate_key()
    with open("mykey.key", "wb") as key_file:
        key_file.write(key)

# 2. LOAD THE KEY
def load_key():
    return open("mykey.key", "rb").read()

# 3. ENCRYPT
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

# 4. DECRYPT
def decrypt_message(encrypted_data, key):
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()

# --- QUICK TEST ---
# generate_key() # Uncomment this the first time you run it!

key = load_key()
secret = encrypt_message("My super secret password", key)
print(f"Encrypted: {secret}")

original = decrypt_message(secret, key)
print(f"Decrypted: {original}")
import json
import os
from cryptography.fernet import Fernet
import secrets
import string
import pyperclip

# Constants
DATA_FILE = 'passwords.json'
KEY_FILE = 'key.key'

# -------------------- Helper Functions --------------------

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_data(data, key):
    f = Fernet(key)
    return f.decrypt(data).decode()

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'rb') as file:
        encrypted_data = file.read()
    try:
        decrypted_data = decrypt_data(encrypted_data, load_key())
        return json.loads(decrypted_data)
    except:
        return {}

def save_data(data):
    key = load_key()
    encrypted_data = encrypt_data(json.dumps(data), key)
    with open(DATA_FILE, 'wb') as file:
        file.write(encrypted_data)

# -------------------- Password Generation --------------------

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    print("Generated password copied to clipboard.")
    return password

# -------------------- Core Functionality --------------------

def add_entry():
    service = input("Enter service name: ").strip()
    username = input("Enter username: ").strip()
    choice = input("Generate password? (y/n): ").strip().lower()
    if choice == 'y':
        password = generate_password()
    else:
        password = input("Enter password: ").strip()

    data = load_data()
    data[service] = {'username': username, 'password': password}
    save_data(data)
    print("Password saved successfully!")

def retrieve_entry():
    service = input("Enter service name to retrieve: ").strip()
    data = load_data()
    if service in data:
        print(f"Username: {data[service]['username']}")
        print(f"Password: {data[service]['password']}")
        pyperclip.copy(data[service]['password'])
        print("Password copied to clipboard.")
    else:
        print("No entry found for that service.")

def list_services():
    data = load_data()
    if data:
        print("Stored services:")
        for service in data:
            print(f"- {service}")
    else:
        print("No services stored.")

# -------------------- Menu --------------------

def main():
    print("\n--- Password Manager ---")
    while True:
        print("\nOptions:")
        print("1. Add new entry")
        print("2. Retrieve password")
        print("3. List services")
        print("4. Generate password")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            add_entry()
        elif choice == '2':
            retrieve_entry()
        elif choice == '3':
            list_services()
        elif choice == '4':
            print("Generated Password:", generate_password())
        elif choice == '5':
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()

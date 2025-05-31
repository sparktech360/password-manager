# 🔐 Password Manager

A simple yet secure password manager built in Python. This tool allows you to safely store, retrieve, and generate strong passwords for all your accounts.

---

## 📦 Features

* ✅ Add and store credentials securely
* 🔐 Encrypt all data using `cryptography`
* 🔑 Generate strong random passwords
* 📋 Auto-copy passwords to clipboard
* 📂 JSON-based local storage
* 🖥️ CLI-based user interface

---

## 🚀 Getting Started

### Prerequisites

* Python 3.7+
* Install dependencies:

```bash
pip install cryptography pyperclip
```

### Run the App

```bash
python password_manager.py
```

---

## 📋 Usage

### Add a New Entry

1. Choose option `1` from the menu
2. Enter the service name and username
3. Choose to auto-generate or manually enter a password

### Retrieve a Password

1. Choose option `2`
2. Enter the service name
3. Username and password will be displayed and copied to clipboard

### Generate a Password

1. Choose option `4`
2. A random password is generated and copied to your clipboard

---

## 🔐 Security

* All password data is encrypted using a key stored in `key.key`
* Data is stored in `passwords.json` (encrypted)

**Note:** Keep your `key.key` file safe — it's required to decrypt your password data.

---

## 📁 File Structure

```
├── password_manager.py
├── passwords.json  # (Encrypted file will be created after saving data)
├── key.key         # (Encryption key)
└── README.md
```

---

## 🛠️ Built With

* [Python](https://www.python.org/)
* [cryptography](https://pypi.org/project/cryptography/)
* [pyperclip](https://pypi.org/project/pyperclip/)

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* Inspired by real-world security needs and personal productivity tools

---

## ✨ Contributions

Feel free to fork the repo and submit pull requests! Suggestions and improvements are always welcome.

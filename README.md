A secure desktop-based password manager application developed using Python, Tkinter, SQLite, and AES encryption (Fernet from the cryptography library). 
The tool allows users to safely store and manage multiple account credentials (usernames and passwords) within a locally encrypted database.
Key Features:

> Master Password Login: Only authenticated users can access the vault using a master password.

> AES Encryption: All stored credentials are encrypted using Fernet (AES-128) encryption, ensuring data privacy.

> Local Database: Uses SQLite (db.sqlite3) to store encrypted credentials securely.

> Add/View/Delete Credentials: Users can add new entries, view saved credentials, or delete them with ease.

> User-Friendly Interface: Built with Tkinter for a simple and intuitive GUI.
Tools & Tech:

Language: Python

GUI: Tkinter

Database: SQLite

Encryption: Cryptography (Fernet - AES)

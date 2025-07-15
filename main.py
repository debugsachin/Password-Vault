import tkinter as tk
from tkinter import messagebox
import sqlite3
from cryptography.fernet import Fernet
import os

# Encryption key (store securely in real app)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# DB setup
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS vault (
    id INTEGER PRIMARY KEY,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)''')
conn.commit()

# GUI
root = tk.Tk()
root.title("Password Vault")

def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if website and username and password:
        encrypted_pw = cipher.encrypt(password.encode())
        cursor.execute("INSERT INTO vault (website, username, password) VALUES (?, ?, ?)",
                       (website, username, encrypted_pw))
        conn.commit()
        messagebox.showinfo("Saved", "Password stored securely!")
    else:
        messagebox.showwarning("Missing info", "All fields are required.")

tk.Label(root, text="Website").pack()
entry_website = tk.Entry(root)
entry_website.pack()

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Save", command=save_password).pack(pady=10)

root.mainloop()

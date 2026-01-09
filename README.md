# Password Strength & Breach Detection Tool (Python + GUI)

A Python-based cybersecurity tool that analyzes password strength and checks whether the entered password has been found in known data breaches using the HaveIBeenPwned™ k-anonymity method.
This project includes a simple and interactive GUI built with Tkinter.

## 📌 Features

✔️ GUI-based interface for user interaction

✔️ Measures password strength based on:
Length
Character diversity
Entropy

✔️ Detects whether the password appears in breached databases

✔️ Provides suggestions to improve security

✔️ Uses SHA-1 hashing and the HIBP k-anonymity model

✔️ Secure password generator using Python's secrets module

✔️ Fast and lightweight
<br>

## 🖥️ Tech Stack

Component -> Technology 

Language: Python

GUI: Tkinter

Networking: Requests

Cryptography: SHA-1 Hashing

API: HaveIBeenPwned (range method)



## 🎯 How It Works

1️⃣ User enters a password

2️⃣ Tool calculates:

-Strength score (0–100)

-Entropy (bits)

3️⃣ Sends the first 5 characters of the hashed password to HIBP API

4️⃣ Searches for matches locally (k-anonymity — safe method)

5️⃣ Displays:

Whether breached
Number of breach occurrences
Improvement suggestions




## 🚀 Installation & Setup

Step 1: Clone the repository-

git clone https://github.com/urvija-kapila/password-checker.git

cd password-checker

Step 2: Install dependencies-

pip install requests

Step 3: Run the GUI-

python gui.py


## 🔐 Security Notes

This tool does NOT send your password anywhere.
It only sends the first 5 characters of its SHA-1 hash, following the k-anonymity principle.

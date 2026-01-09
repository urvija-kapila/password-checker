import tkinter as tk
from tkinter import messagebox
from checker import password_strength
from breach import check_breach

# GUI window
window = tk.Tk()
window.title("Password Strength & Breach Checker")
window.geometry("550x420")
window.resizable(False, False)

# Heading
heading = tk.Label(window, text="Password Analyzer", font=("Arial", 18, "bold"))
heading.pack(pady=15)

# Input label
label = tk.Label(window, text="Enter Password:", font=("Arial", 12))
label.pack()

# Input box
password_entry = tk.Entry(window, width=40, font=("Arial", 14), show="*")
password_entry.pack(pady=10)

# Output text box
output_box = tk.Text(window, height=10, width=60, font=("Consolas", 10))
output_box.pack(pady=15)

def analyze_password():
    pwd = password_entry.get().strip()
    if not pwd:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    output_box.delete(1.0, tk.END)

    score, entropy, remarks = password_strength(pwd)
    breach_count = check_breach(pwd)

    output_box.insert(tk.END, f"Strength Score: {score}/100\n")
    output_box.insert(tk.END, f"Entropy: {entropy} bits\n\n")

    if breach_count > 0:
        output_box.insert(tk.END, f"⚠️ WARNING: Found {breach_count} times in breaches.\n\n")
    else:
        output_box.insert(tk.END, "✔️ Not found in any known breaches.\n\n")

    if remarks:
        output_box.insert(tk.END, "Suggestions:\n")
        for r in remarks:
            output_box.insert(tk.END, f"- {r}\n")

# Button
btn = tk.Button(window, text="Analyze Password", font=("Arial", 12, "bold"),
                command=analyze_password, bg="#0A84FF", fg="white", width=20)
btn.pack(pady=5)

window.mainloop()

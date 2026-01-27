import tkinter as tk
from tkinter import messagebox
from checker import password_strength
from breach import check_breach
from generator import generate_password

# GUI window
window = tk.Tk()
window.title("Password Strength & Breach Checker")
window.geometry("550x520")
window.resizable(False, False)

# Heading
heading = tk.Label(window, text="Password Analyzer", font=("Arial", 18, "bold"))
heading.pack(pady=15)

# Input label
label = tk.Label(window, text="Enter Password :", font=("Arial", 12))
label.pack()

# Input box
password_entry = tk.Entry(window, width=40, font=("Arial", 14), show="*")
password_entry.pack(pady=10)

# Output text box
output_box = tk.Text(window, height=5, width=60, font=("Consolas", 10))
output_box.pack(pady=15)

#analyze frame
analyze_frame = tk.Frame(window)
analyze_frame.pack(pady=10)

# Length Label
generator_frame = tk.Frame(window)
generator_frame.pack(pady=10)
generator_frame.grid_columnconfigure(0, weight=1)

#button label
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

length_label = tk.Label(
    generator_frame,
    text="Password Length",
    font=("Arial", 11, "bold")
)
length_label.grid(row=0, column=0, pady=5)

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

def generate_and_fill():
    length = length_slider.get()
    pwd = generate_password(length)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, pwd)

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "✔️ Secure password generated.\nClick 'Analyze Password' to evaluate it.\n")

def copy_to_clipboard():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showwarning("Warning", "No password to copy.")
        return

    window.clipboard_clear()
    window.clipboard_append(pwd)
    window.update()

    messagebox.showinfo("Copied", "Password copied to clipboard!")


def update_length(val):
    length_label.config(text=f"Password Length: {val}")



# analyse Button
analyze_btn = tk.Button(
    analyze_frame,
    text="Analyze Password",
    font=("Arial", 12, "bold"),
    command=analyze_password,
    bg="#1D5389",
    fg="white",
    width=22
)
analyze_btn.grid(row=0, column=0, padx=10, pady=5)

#length slider 
length_slider = tk.Scale(
    generator_frame,
    from_=8,
    to=24,
    orient="horizontal"
)
length_slider.set(12)
length_slider.grid(row=1, column=0, padx=10)

#generate button
gen_btn = tk.Button(
    button_frame,
    text="Generate Strong Password",
    font=("Arial", 12, "bold"),
    command=generate_and_fill,
    bg="#34C759",
    fg="white",
    width=22
)
gen_btn.grid(row=0, column=1, padx=10, pady=5)


#copy button
copy_btn = tk.Button(
    button_frame,
    text="Copy to Clipboard",
    font=("Arial", 12, "bold"),
    command=copy_to_clipboard,
    bg="#FF9F0A",
    fg="white",
    width=22
)
copy_btn.grid(row=1, column=0, columnspan=2, pady=8)




window.mainloop()

import tkinter as tk
from tkinter import messagebox
import random
import string

# تابع تولید پسورد
def generate_password():
    length = int(length_entry.get())
    
    # تنظیمات انتخاب شده توسط کاربر
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()
    
    if not (include_upper or include_lower or include_digits or include_symbols):
        messagebox.showwarning("Warning", "Please select at least one character type!")
        return
    
    char_pool = ""
    
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# طول پسورد
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # طول پیش‌فرض

# گزینه‌های کاراکترها
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var)
upper_check.pack(pady=2)

lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var)
lower_check.pack(pady=2)

digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack(pady=2)

symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_check.pack(pady=2)

# دکمه تولید پسورد
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# نمایش پسورد تولید شده
password_entry = tk.Entry(root, font=("Arial", 14))
password_entry.pack(pady=10)

# اجرای برنامه
root.mainloop()

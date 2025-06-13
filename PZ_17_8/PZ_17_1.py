# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sign Up")
root.geometry('500x560')
root.configure(bg='#191e38')

style = ttk.Style()
style.theme_use('clam')

style.configure('TFrame', background='#191e38')
style.configure('TLabel', background='#191e38', foreground='#ffff00', font=('Arial', 10))
style.configure('TEntry', fieldbackground='white', foreground='gray')
style.configure('TCombobox', fieldbackground='white', foreground='gray')
style.configure('TCheckbutton', background='#191e38', foreground='#ffff00')
style.configure('TRadiobutton', background='#191e38', foreground='#ffff00')

style.configure('Rounded.TButton',
               background='#4CAF50',
               foreground='white',
               font=('Arial', 10, 'bold'),
               borderwidth=0,
               focusthickness=3,
               focuscolor='#4CAF50',
               relief='raised',
               padding=10,
               bordercolor='#4CAF50')
style.map('Rounded.TButton',
          background=[('active', '#45a049')])

style.configure('Red.Rounded.TButton',
               background='#F44336',
               foreground='white',
               font=('Arial', 10, 'bold'),
               borderwidth=0,
               focusthickness=3,
               focuscolor='#F44336',
               relief='raised',
               padding=10,
               bordercolor='#F44336')
style.map('Red.Rounded.TButton',
          background=[('active', '#d32f2f')])

style.layout('Rounded.TButton', [
    ('Button.border', {'children':
        [('Button.focus', {'children':
            [('Button.padding', {'children':
                [('Button.label', {'side': 'left', 'expand': 1})]
    })]})]})])

style.layout('Red.Rounded.TButton', [
    ('Button.border', {'children':
        [('Button.focus', {'children':
            [('Button.padding', {'children':
                [('Button.label', {'side': 'left', 'expand': 1})]
    })]})]})])

top_line = tk.Frame(root, bg='#FF9900', height=50)
top_line.pack(fill='x', pady=(0, 20))

title_label = tk.Label(top_line, text="Sign Up", bg='#FF9900', fg='#FFFF99',
                     font=('Arial', 16, 'bold'))
title_label.pack(side='left', padx=20, pady=10)

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True, fill='both', padx=50)

row_counter = 1

fields_part1 = [
    ("First Name", "Enter First Name..."),
    ("Last Name", "Enter Last Name..."),
    ("Screen Name", "Enter Screen Name..."),
]

for field in fields_part1:
    label_text, placeholder = field
    ttk.Label(main_frame, text=label_text).grid(row=row_counter, column=0, sticky="w", pady=5, padx=10)
    entry = ttk.Entry(main_frame, width=35)
    entry.grid(row=row_counter, column=1, pady=5, padx=10)
    entry.insert(0, placeholder)
    entry.config(foreground='gray')
    row_counter += 1

ttk.Label(main_frame, text="Date of Birth").grid(row=row_counter, column=0, sticky="w", pady=5, padx=10)
dob_frame = ttk.Frame(main_frame)
dob_frame.grid(row=row_counter, column=1, sticky="w")

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
month_cb = ttk.Combobox(dob_frame, values=months, width=10, state="readonly")
month_cb.set("May")
month_cb.pack(side="left")

day_spin = ttk.Spinbox(dob_frame, from_=1, to=31, width=4)
day_spin.set(5)
day_spin.pack(side="left", padx=5)

year_spin = ttk.Spinbox(dob_frame, from_=1900, to=2023, width=6)
year_spin.set(1985)
year_spin.pack(side="left")

row_counter += 1

ttk.Label(main_frame, text="Gender").grid(row=row_counter, column=0, sticky="w", pady=5, padx=10)
gender_frame = ttk.Frame(main_frame)
gender_frame.grid(row=row_counter, column=1, sticky="w")

gender_var = tk.StringVar(value="Male")
ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left", padx=10)

row_counter += 1

ttk.Label(main_frame, text="Country").grid(row=row_counter, column=0, sticky="w", pady=5, padx=10)
countries = ["USA", "Canada", "UK", "Australia", "Germany", "France", "Japan", "Brazil"]
country_cb = ttk.Combobox(main_frame, values=countries, width=33, state="readonly")
country_cb.set("USA")
country_cb.grid(row=row_counter, column=1, sticky="w", padx=10)

row_counter += 1

fields_part2 = [
    ("E-mail", "Enter E-mail......"),
    ("Phone", "Enter Phone......"),
]

for field in fields_part2:
    label_text, placeholder = field
    ttk.Label(main_frame, text=label_text).grid(row=row_counter, column=0, sticky="w", pady=5, padx=10)
    entry = ttk.Entry(main_frame, width=35)
    entry.grid(row=row_counter, column=1, pady=5, padx=10)
    entry.insert(0, placeholder)
    entry.config(foreground='gray')
    row_counter += 1

ttk.Label(main_frame, text="Password").grid(row=row_counter, column=0, sticky="w", pady=6, padx=10)
ttk.Entry(main_frame, width=35, show="*").grid(row=row_counter, column=1, pady=5, padx=10)

row_counter += 1

ttk.Label(main_frame, text="Confirm Password").grid(row=row_counter, column=0, sticky="w", pady=5, padx=10)
ttk.Entry(main_frame, width=35, show="*").grid(row=row_counter, column=1, pady=5, padx=10)

row_counter += 1

terms_var = tk.IntVar()
ttk.Checkbutton(main_frame, text="I agree to the Terms of Use", variable=terms_var).grid(
    row=row_counter, column=0, columnspan=2, pady=20)

row_counter += 1

bottom_line = tk.Frame(root, bg='#FF9900', height=60)
bottom_line.pack(fill='x', pady=(20, 0), side='bottom')

buttons_frame = tk.Frame(bottom_line, bg='#FF9900')
buttons_frame.pack(side='right', padx=20, pady=10)

submit_btn = ttk.Button(buttons_frame, text="Submit", style='Rounded.TButton')
submit_btn.pack(side='left', padx=10)

cancel_btn = ttk.Button(buttons_frame, text="Cancel", command=root.destroy, style='Red.Rounded.TButton')
cancel_btn.pack(side='left', padx=10)

for widget in main_frame.winfo_children():
    if isinstance(widget, ttk.Frame):
        widget.configure(style='TFrame')

root.mainloop()

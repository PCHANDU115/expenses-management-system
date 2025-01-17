import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to create the database and table (if not already created)
def create_db():
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT,
                        category TEXT,
                        amount REAL,
                        date TEXT)''')
    conn.commit()
    conn.close()

# Function to add an expense to the database
def add_expense(description, category, amount, date):
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO expenses (description, category, amount, date)
                      VALUES (?, ?, ?, ?)''', (description, category, amount, date))
    conn.commit()
    conn.close()

# Function to fetch expenses within a specific date range
def fetch_expenses(start_date, end_date):
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM expenses WHERE date BETWEEN ? AND ?''', (start_date, end_date))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to plot the expense data
def plot_expenses(data):
    df = pd.DataFrame(data, columns=['ID', 'Description', 'Category', 'Amount', 'Date'])
    df['Date'] = pd.to_datetime(df['Date'])  # Convert the 'Date' column to datetime

    # Plot total expenses by category using Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Amount', data=df, palette='viridis')
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    
    # Embed the plot into the Tkinter window
    canvas = FigureCanvasTkAgg(plt.gcf(), master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Function to update the plot based on date range
def update_plot():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    if start_date and end_date:
        expenses = fetch_expenses(start_date, end_date)
        if expenses:
            plot_expenses(expenses)
        else:
            messagebox.showwarning("No Data", "No expenses found in this date range.")
    else:
        messagebox.showerror("Input Error", "Please enter both start and end dates.")

# Function to add custom expenses
def add_custom_expense():
    description = description_entry.get()
    category = category_combobox.get()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")
        return
    date = date_entry.get()

    if description and category and amount and date:
        add_expense(description, category, amount, date)
        messagebox.showinfo("Expense Added", "Your expense has been added successfully.")
        description_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Input Error", "Please fill in all fields.")

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")

# Frame for input fields and buttons
input_frame = tk.Frame(root)
input_frame.pack(side=tk.LEFT, padx=20, pady=20)

# Expense Category Input
tk.Label(input_frame, text="Category:", font=("Arial", 12)).pack(pady=5)
category_combobox = ttk.Combobox(input_frame, font=("Arial", 12), values=["Food", "Entertainment", "Health", "Transport", "Others"])
category_combobox.pack(pady=5)

# Expense Amount Input
tk.Label(input_frame, text="Amount:", font=("Arial", 12)).pack(pady=5)
amount_entry = tk.Entry(input_frame, font=("Arial", 12))
amount_entry.pack(pady=5)

# Expense Date Input
tk.Label(input_frame, text="Date (YYYY-MM-DD):", font=("Arial", 12)).pack(pady=5)
date_entry = tk.Entry(input_frame, font=("Arial", 12))
date_entry.pack(pady=5)

# Add Custom Expense Button
add_expense_button = tk.Button(input_frame, text="Add Expense", command=add_custom_expense, font=("Arial", 12))
add_expense_button.pack(pady=10)

# Start Date Input
tk.Label(input_frame, text="Start Date (YYYY-MM-DD):", font=("Arial", 12)).pack(pady=5)
start_date_entry = tk.Entry(input_frame, font=("Arial", 12))
start_date_entry.pack(pady=5)

# End Date Input
tk.Label(input_frame, text="End Date (YYYY-MM-DD):", font=("Arial", 12)).pack(pady=5)
end_date_entry = tk.Entry(input_frame, font=("Arial", 12))
end_date_entry.pack(pady=5)

# Update Plot Button
update_button = tk.Button(input_frame, text="Show Expenses", command=update_plot, font=("Arial", 12))
update_button.pack(pady=10)

# Frame for displaying the plot
plot_frame = tk.Frame(root)
plot_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH, expand=True)

# Start the database and create table if needed
create_db()

# Run the Tkinter GUI
root.mainloop()

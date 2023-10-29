import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database setup
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_number INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        account_type TEXT,
        balance REAL,
        phone_number TEXT,
        address TEXT,
        email TEXT,
        last_transaction REAL
    )
''')
conn.commit()

# List of predefined accounts
# Database setup for predefined accounts
predefined_conn = sqlite3.connect('predefined_accounts.db')
predefined_cursor = predefined_conn.cursor()
predefined_accounts = [
    (1001, "Parvinder Singh", 30, "Male", "Savings", 500000.0, "123-456-7890", "Powai", "singh@email.com",
     "4999.0 debited"),
    (1002, "Sia Shah", 25, "Female", "Savings", 79000.0, "987-654-3210", "Borivali East", "sshah@email.com",
     "7500.0 credited"),
    (1003, "Deep Sharma", 27, "Male", "Current", 99000.0, "987-654-3890", "Andheri West", "ssdeep@email.com",
     "29.0 credited"),
    (1004, "Rohan", 39, "Male", "Savings", 45000.0, "987-654-3778", "Malad West", "coolrohan@email.com",
     "20000.0 debited"),
    (1005, "Rekha Rao", 34, "Female", "Salary", 7909000.0, "987-654-6789", "Bandra", "rrao@email.com",
     "75000.0 credited"),
    (1006, "Shreya Vora", 42, "Female", "Savings", 8020.0, "987-654-3760", "Mira Road", "shreyav@email.com",
     "45200 credited"),
    (1007, "Meghna verma", 66, "Female", "Savings", 7800000.0, "987-634-9076", "Santa Cruz", "mvrm@email.com",
     "15000 debited"),
    (1008, "Dev Patel", 56, "Male", "Current", 12000.0, "987-654-6666", "Thane", "dp1998@email.com",
     "740.0 credited"),
    (1009, "Ruh Gupta", 19, "Female", "Saving", 12500000.0, "987-654-3210", "Bandra", "gupta@email.com",
     "50.0 credited"),
    (10010, "Jay Sanil", 24, "Male", "Salary", 790.0, "987-654-3110", "Vasai", "sanil@email.com",
     "60000.0 credited"),
    (10011, "Saee Sawant", 76, "Female", "Savings", 988800.0, "987-854-3110", "Jogeshwari", "ssawant@email.com",
     "60800.0 debited"),
    (10012, "Dhruva Shah", 28, "Female", "Salary", 19040000.0, "987-654-3010", "Worli", "riyans@email.com",
     "340000.0 credited"),
    (10013, "Jeet Sawant", 78, "Male", "Salary", 5900000.0, "987-654-4112", "Sea Woods", "lavanya@email.com",
     "60.0 credited"),
    (10014, "Vipul Gandhi", 36, "Male", "Current", 199900.0, "987-687-3110", "Bhayander", "vgandhi@email.com",
     "23.0 debited"),

]

# Function to add predefined accounts if they don't exist in the database
def add_predefined_accounts():

    for account in predefined_accounts:
        account_number = account[0]
        cursor.execute("SELECT account_number FROM accounts WHERE account_number = ?", (account_number,))
        existing_account = cursor.fetchone()
        if not existing_account:
            cursor.execute("INSERT INTO accounts VALUES (?,?,?,?,?,?,?,?,?,?)", account)

    conn.commit()

add_predefined_accounts()
# Function to create a new bank account and add to both databases
def create_account():
    def submit():
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_var.get()
        account_type = account_type_entry.get()
        balance = balance_entry.get()
        phone_number = phone_entry.get()
        address = address_entry.get()
        email = email_entry.get()

        try:
            balance = float(balance)

            # Add to the main database
            cursor.execute(
                "INSERT INTO accounts (name, age, gender, account_type, balance, phone_number, address, email, last_transaction) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (name, age, gender, account_type, balance, phone_number, address, email, balance))
            conn.commit()

            # Add to the predefined accounts database
            predefined_cursor.execute(
                "INSERT INTO accounts (account_number, name, age, gender, account_type, balance, phone_number, address, email, last_transaction) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (None, name, age, gender, account_type, balance, phone_number, address, email, balance))
            predefined_conn.commit()

            messagebox.showinfo("Success", "Account created successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid balance. Please enter a valid number.")

    account_window = tk.Toplevel(main_window)
    account_window.title("Create Account")
    account_window.configure(bg="#ADD8E6")

    name_label = tk.Label(account_window, text="Name:", bg="#ADD8E6", fg="black")
    name_label.pack()
    name_entry = tk.Entry(account_window)
    name_entry.pack()

    age_label = tk.Label(account_window, text="Age:", bg="#ADD8E6", fg="black")
    age_label.pack()
    age_entry = tk.Entry(account_window)
    age_entry.pack()

    gender_label = tk.Label(account_window, text="Gender:", bg="#ADD8E6", fg="black")
    gender_label.pack()
    gender_var = tk.StringVar()
    gender_var.set("Male")  #
    gender_optionmenu = tk.OptionMenu(account_window, gender_var, "Male", "Female", "Other")
    gender_optionmenu.pack()

    account_type_label = tk.Label(account_window, text="Account Type:", bg="#ADD8E6", fg="black")
    account_type_label.pack()
    account_type_entry = tk.Entry(account_window)
    account_type_entry.pack()

    balance_label = tk.Label(account_window, text="Initial Balance:", bg="#ADD8E6", fg="black")
    balance_label.pack()
    balance_entry = tk.Entry(account_window)
    balance_entry.pack()

    phone_label = tk.Label(account_window, text="Phone Number:", bg="#ADD8E6", fg="black")
    phone_label.pack()
    phone_entry = tk.Entry(account_window)
    phone_entry.pack()

    address_label = tk.Label(account_window, text="Address:", bg="#ADD8E6", fg="black")
    address_label.pack()
    address_entry = tk.Entry(account_window)
    address_entry.pack()

    email_label = tk.Label(account_window, text="Email:", bg="#ADD8E6", fg="black")
    email_label.pack()
    email_entry = tk.Entry(account_window)
    email_entry.pack()

    submit_button = tk.Button(account_window, text="Create Account", command=submit, bg="#dafdb3", fg="black")
    submit_button.pack()

# Function to deposit money
def deposit():
    def submit():
        account_number = account_number_entry.get()
        amount = amount_entry.get()

        try:
            account_number = int(account_number)
            amount = float(amount)

            # Update balance in the main database
            cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
            current_balance = cursor.fetchone()[0]
            new_balance = current_balance + amount
            cursor.execute("UPDATE accounts SET balance = ?, last_transaction = ? WHERE account_number = ?", (new_balance, amount, account_number))
            conn.commit()

            # Update balance in the predefined accounts database
            predefined_cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
            current_balance = predefined_cursor.fetchone()[0]
            new_balance = current_balance + amount
            predefined_cursor.execute("UPDATE accounts SET balance = ?, last_transaction = ? WHERE account_number = ?", (new_balance, amount, account_number))
            predefined_conn.commit()

            messagebox.showinfo("Success", "Amount deposited successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid account number or amount.")

    deposit_window = tk.Toplevel(main_window)
    deposit_window.title("Deposit Money")
    deposit_window.configure(bg="#ADD8E6")

    account_number_label = tk.Label(deposit_window, text="Account Number:", bg="#ADD8E6", fg="black")
    account_number_label.pack()
    account_number_entry = tk.Entry(deposit_window)
    account_number_entry.pack()

    amount_label = tk.Label(deposit_window, text="Amount:", bg="#ADD8E6", fg="black")
    amount_label.pack()
    amount_entry = tk.Entry(deposit_window)
    amount_entry.pack()

    submit_button = tk.Button(deposit_window, text="Deposit", command=submit, bg="#dafdb3", fg="black")
    submit_button.pack()

# Function to withdraw money
def withdraw():
    def submit():
        account_number = account_number_entry.get()
        amount = amount_entry.get()

        try:
            account_number = int(account_number)
            amount = float(amount)

            # Update balance in the main database
            cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
            current_balance = cursor.fetchone()[0]
            if current_balance >= amount:
                new_balance = current_balance - amount
                cursor.execute("UPDATE accounts SET balance = ?, last_transaction = ? WHERE account_number = ?", (new_balance, -amount, account_number))
                conn.commit()

                # Update balance in the predefined accounts database
                predefined_cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
                current_balance = predefined_cursor.fetchone()[0]
                if current_balance >= amount:
                    new_balance = current_balance - amount
                    predefined_cursor.execute("UPDATE accounts SET balance = ?, last_transaction = ? WHERE account_number = ?", (new_balance, -amount, account_number))
                    predefined_conn.commit()

                    messagebox.showinfo("Success", "Amount withdrawn successfully.")
                else:
                    messagebox.showerror("Error", "Insufficient balance in the predefined account.")
            else:
                messagebox.showerror("Error", "Insufficient balance.")
        except ValueError:
            messagebox.showerror("Error", "Invalid account number or amount.")

    withdraw_window = tk.Toplevel(main_window)
    withdraw_window.title("Withdraw Money")
    withdraw_window.configure(bg="#ADD8E6")

    account_number_label = tk.Label(withdraw_window, text="Account Number:", bg="#ADD8E6", fg="black")
    account_number_label.pack()
    account_number_entry = tk.Entry(withdraw_window)
    account_number_entry.pack()

    amount_label = tk.Label(withdraw_window, text="Amount:", bg="#ADD8E6", fg="black")
    amount_label.pack()
    amount_entry = tk.Entry(withdraw_window)
    amount_entry.pack()

    submit_button = tk.Button(withdraw_window, text="Withdraw", command=submit, bg="red", fg="black")
    submit_button.pack()

# Function to transfer money
def transfer():
    def submit():
        from_account = from_account_entry.get()
        to_account = to_account_entry.get()
        amount = amount_entry.get()

        try:
            from_account = int(from_account)
            to_account = int(to_account)
            amount = float(amount)

            # Update balance in the main database for the source account
            cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (from_account,))
            from_balance = cursor.fetchone()[0]
            if from_balance >= amount:
                new_from_balance = from_balance - amount
                cursor.execute("UPDATE accounts SET balance = ?, last_transaction = ? WHERE account_number = ?", (new_from_balance, -amount, from_account))
                conn.commit()

                # Update balance in the main database for the target account
                cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (to_account,))
                to_balance = cursor.fetchone()[0]
                new_to_balance = to_balance + amount
                cursor.execute("UPDATE accounts SET balance = ?, last_transaction = ? WHERE account_number = ?", (new_to_balance, amount, to_account))
                conn.commit()

                # Update balance in the predefined accounts database for the source account
                predefined_cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (from_account,))
                from_balance = predefined_cursor.fetchone()[0]
                if from_balance >= amount:
                    new_from_balance = from_balance - amount
                    predefined_cursor.execute("UPDATE accounts SET balance = ?, last_transaction = ? WHERE account_number = ?", (new_from_balance, -amount, from_account))
                    predefined_conn.commit()

                    # Update balance in the predefined accounts database for the target account
                    predefined_cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (to_account,))
                    to_balance = predefined_cursor.fetchone()[0]
                    new_to_balance = to_balance + amount
                    predefined_cursor.execute("UPDATE accounts SET balance = ?, last_transaction = ? WHERE account_number = ?", (new_to_balance, amount, to_account))
                    predefined_conn.commit()

                    messagebox.showinfo("Success", "Amount transferred successfully.")
                else:
                    messagebox.showerror("Error", "Insufficient balance in the source account (predefined).")
            else:
                messagebox.showerror("Error", "Insufficient balance in the source account.")
        except ValueError:
            messagebox.showerror("Error", "Invalid account numbers or amount.")

    transfer_window = tk.Toplevel(main_window)
    transfer_window.title("Transfer Money")
    transfer_window.configure(bg="#ADD8E6")

    from_account_label = tk.Label(transfer_window, text="From Account Number:", bg="#ADD8E6", fg="black")
    from_account_label.pack()
    from_account_entry = tk.Entry(transfer_window)
    from_account_entry.pack()

    to_account_label = tk.Label(transfer_window, text="To Account Number:", bg="#ADD8E6", fg="black")
    to_account_label.pack()
    to_account_entry = tk.Entry(transfer_window)
    to_account_entry.pack()

    amount_label = tk.Label(transfer_window, text="Amount:", bg="#ADD8E6", fg="black")
    amount_label.pack()
    amount_entry = tk.Entry(transfer_window)
    amount_entry.pack()

    submit_button = tk.Button(transfer_window, text="Transfer", command=submit, bg="#FFA500", fg="black")
    submit_button.pack()

# Function to check balance
def check_balance():
    def submit():
        account_number = account_number_entry.get()
        try:
            account_number = int(account_number)
            if account_number <= 0:
                messagebox.showerror("Error", "Invalid account number.")
            else:
                # First, check the main database
                cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
                current_balance = cursor.fetchone()

                if current_balance:
                    formatted_balance = "{:,.2f}".format(current_balance[0])
                    messagebox.showinfo("Balance", f"Current balance: ₹{formatted_balance}")
                else:
                    # If not found in the main database, check the predefined accounts
                    predefined_cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
                    predefined_balance = predefined_cursor.fetchone()

                    if predefined_balance:
                        formatted_balance = "{:,.2f}".format(predefined_balance[0])
                        messagebox.showinfo("Balance", f"Current balance (predefined): ₹{formatted_balance}")
                    else:
                        messagebox.showerror("Error", "Account not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid account number.")

    balance_window = tk.Toplevel(main_window)
    balance_window.title("Check Balance")
    balance_window.configure(bg="#ADD8E6")

    account_number_label = tk.Label(balance_window, text="Account Number:", bg="#1E90FF", fg="white")
    account_number_label.pack()
    account_number_entry = tk.Entry(balance_window)
    account_number_entry.pack()

    submit_button = tk.Button(balance_window, text="Check Balance", command=submit, bg="#FFD700", fg="white")
    submit_button.pack()

# Main menu
main_window = tk.Tk()
main_window.title("Bank Management System")
main_window.configure(bg="#ADD8E6")  # Set the background color

welcome_label = tk.Label(main_window, text="Welcome to the Bank Management System", font=("Times New Roman", 16), fg="black")
welcome_label.grid(row=0)

create_account_button = tk.Button(main_window, text="Create Account", command=create_account, bg="#FFE5A8", fg="black", font=("Courier", 12))
create_account_button.grid(row=1, column=0, padx=10, pady=10)

deposit_button = tk.Button(main_window, text="Deposit Money", command=deposit, bg="#F8FF97", fg="black", font=("Courier", 12))
deposit_button.grid(row=5, column=0, padx=10, pady=10)

withdraw_button = tk.Button(main_window, text="Withdraw Money", command=withdraw, bg="#BCFFA4", fg="black", font=("Courier", 12))
withdraw_button.grid(row=7, column=0, padx=10, pady=10)

transfer_button = tk.Button(main_window, text="Transfer Money", command=transfer, bg="#A6FFD3", fg="black",  font=("Courier", 12))
transfer_button.grid(row=9, column=0, padx=10, pady=10)

check_balance_button = tk.Button(main_window, text="Check Balance", command=check_balance, bg="#C1CCFF", fg="black", font=("Courier", 12))
check_balance_button.grid(row=11, column=0, padx=10, pady=10)

main_window.mainloop()

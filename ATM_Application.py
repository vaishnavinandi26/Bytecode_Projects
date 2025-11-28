#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("=== Welcome to UNION Bank ATM ===")

balance = 50000
correct_pin = "2004"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access Granted!")
        break
    else:
        attempts += 1
        if attempts == max_attempts:
            print("Card Blocked!")
            exit()
        else:
            print(f"Wrong PIN! {max_attempts - attempts} attempts left.")
            
while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Change PIN")
    print("5. Exit")

    ch = input("Choose (1-5): ")

    if ch == "1":
        print(f"Your balance: ₹{balance}")

    elif ch == "2":
        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount % 100 != 0:
            print("Amount must be a multiple of 100!")
        elif amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print(f"Please collect your cash.")
            print(f"New balance: ₹{balance}")

    elif ch == "3":
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount!")
        else:
            balance += amount
            print(f"Amount deposited successfully!")
            print(f"New balance: ₹{balance}")

    elif ch == "4":
        old = input("Enter old PIN: ")
        if old == correct_pin:
            new = input("Enter new 4-digit PIN: ")
            if len(new) == 4 and new.isdigit():
                correct_pin = new
                print("PIN Changed Successfully!")
            else:
                print("PIN must be exactly 4 digits!")
        else:
            print("Incorrect old PIN!")

    elif ch == "5":
        print("Thank You!")
        break

    else:
        print("Invalid choice! Choose between 1-5.")


# In[ ]:





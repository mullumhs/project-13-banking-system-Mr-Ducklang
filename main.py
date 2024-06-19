""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: main.py
# Description: Contains the user interface for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#import classes
from account import Account
from bank import BankManager


#define user_input functions

#add_account
def add_account_ui(manager):
    name = input("New Account name: ")
    balance = 0
    password = input("Account Password: ")
    if manager.add_account(name):
        print(f"New Account: {name}, has been added!")
    else:
        print("Error! Account not added!")
#remove_account
def remove_account_ui(manager):
    name = input("Name of account to remove:")
    if manager.remove_account(name):
        print(f"The Account: {name}, has been removed")
    else:
        print()

#deposit money
def deposit_money_ui(manager):
    deposit_amount = float(input("How much is being deposited? "))
    name = input(f"Deposit ${deposit_amount} into which account? ")
    if manager.deposits(name, deposit_amount):
        print(f"Successfully deposited ${deposit_amount} into {name}")
    else:
        print("Error, could not deposit money, was account name entered correctly?")
    
#withdraw money
def withdraw_money_ui(manager):
    withdraw_amount = float(input("How much is being withdrawn ? "))
    name = input(f"Withdraw ${withdraw_amount} from which account? ")
    if manager.withdrawals(name, withdraw_amount):
        print(f"Successfully withdrew ${withdraw_amount} from {name}")
    else:
        print("Error! Could not withdraw money, was account name entered correctly?")

#transfer money
def transfer_money_ui(manager):
    transfer_amount = float(input("How much is being transferred? "))
    name1 = print(f"Withdraw ${transfer_amount} from which account? ")
    name2 = print(f"Transfer ${transfer_amount}to which account? ")
    if manager.transfers(name1, name2, transfer_amount):
        print(f"Successfully transferred ${transfer_amount} from {name1} into {name2}")
    else:
        print("Could not transfer money, no changes have been made to account amounts.")

#define other functions

#display accounts
def display_accounts(manager):
    manager.display_accounts()
    choice = input("Enter any key to return to menu: ")

#main
def main():
    #define manager
    manager = BankManager()
    
    #map inputs to functions
    actions = {
        '1' : add_account_ui,
        '2' : remove_account_ui,
        '3' : display_accounts,
        '4' : deposit_money_ui,
        '5' : withdraw_money_ui,
        '6' : transfer_money_ui,
        '7' : print("Feature not yet available."),
    }
    
    while True:
        print("\nBank Management System")
        print("1. Add Account")
        print("2. Remove Account")
        print("3. Display All Accounts")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Transfer Money")
        print("7. Manage Accounts (*COMING SOON*)")
        print("8. Exit\n")
        user_choice = input("Enter choice: ")
        print()

    #implement ability to call functions based on input
        if user_choice == '5':
            print('Exiting Program...Goodybe!')
            break
        elif user_choice in actions:
            actions[user_choice](manager)
        else:
            print("Error! Invalid Choice! Please select an option from 1 to 8!")

if __name__ == "__main__":
    main()
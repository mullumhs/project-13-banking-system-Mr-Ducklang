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
    if manager.add_account(Account):
        print(f"New Account: {name}, has been added!")
    else:
        print("Error! Account not added!")
#remove_account
def remove_account_ui(manager):
    name = input("Name of account to remove:")
    if manager.remove_account(Account):
        print(f"The Account: {name}, has been removed")
    else:
        print("Error! Account not removed")

#deposit money


#withdraw money


#transfer money



#define other functions

#display accounts

#main
def main():
    
    manager = BankManager()
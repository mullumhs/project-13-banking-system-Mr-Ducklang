""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#import Account Class
from account import Account

#BankManager Class
class BankManager:
    def __init__(self):
        self.accounts = []
        
    #adding accounts
    def add_account(self, account):
        #check for duplicate
        for existing_account in self.accounts:
            if existing_account.get_name() == self.accounts():
                print("Error, this account name already exists, account not added")
                return False
        #making account
        self.accounts.append(account)
        return True
            
    #removing account
    def remove_account(self, name):
        for i, existing_account in enumerate(self.accounts):
            if existing_account.get_name() == name:
                del self.accounts[i]
                return True
        print("Error! Account not found")
        return False
    
    #managing deposits, withdrawals and transfers
    def manage_transactions():
        print()
        
    #manage account balance, name, passwords
    def manage_accounts():
        print()
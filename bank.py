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
           
    def acc_check(self, name):
        for existing_account in self.accounts:
            if existing_account.get_name() == name:
                return existing_account
        return None 
   
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
    def deposits(self, name, deposit_amount):
        existing_account = self.acc_check(name)
        if existing_account is not None:
            existing_account.deposit(deposit_amount)
            return True
        print("Error! Account not found")
        return False
    
    def withdrawals(self, name, withdraw_amount):
        existing_account = self.acc_check(name)
        if existing_account is not None:
            existing_account.withdraw(withdraw_amount)
            return True
        print("Error! Account not found")
        return False
    
    #transfers 
    def transfers(self, name1, name2, transfer_amount):
        existing_account = self.acc_check(name1)
        existing_account2 = self.acc_check(name2)
        if existing_account is not None and existing_account2 is not None:
            try:
                existing_account.withdraw(transfer_amount)
            except ValueError as e:
                print(e)
            existing_account2.deposit(transfer_amount)
            return True
        if existing_account is None:
            print(f"Error! {name1} not found")
        if existing_account2 is None:
            print(f"Error! {name2} not found")
        return False
            
    #manage account balance, name, passwords
    def manage_acc_name():
        print()
        
    def manage_acc_password():
        print()
 
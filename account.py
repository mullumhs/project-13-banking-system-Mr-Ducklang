""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Account Class
class Account:
    def __init__(self, name, balance, password, ):
        self.set_name(name)
        self.set_balance(balance)
        self._password = password
        
        
#Getters
    def get_name(self):
        return self._name

    def get_balance(self):
        return f"${self._balance:.2f}"

    def get_password(self):
        return self._password

    #Setters
    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Error! New name is not a string!")
        self._name = new_name
        
    def set_balance(self, new_balance):
        if new_balance is str:
            raise ValueError("Error! New Balance must be a number!")
        self._balance = new_balance
   
    def set_password(self, new_password):
        user_input = input("What is your current password?")
        if user_input is self._password:
            self._password = new_password
        else:
            ("Incorrect Password!")


    #Methods
    
    def deposit(self, deposit):
        self.get_balance()
        self._balance = self._balance + deposit
        
    def withdraw(self, withdrawal):
        self.get_balance()
        if withdrawal > self.balance:
            raise ValueError(f"Error! Cannot withdraw more than account balance!, your account balance is {self._balance}")
        self._balance = self._balance - withdrawal
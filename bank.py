import random
class MainBankAccount():
    """Main bank account"""

    def __init__(self, name, last_name, pesel, account_balance = 0):
        self._name = name
        self._last_name = last_name
        self._pesel = pesel
        self._account_balance = account_balance
    

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def last_name(self):
        return self._last_name
    @name.setter
    def name(self, new_last_name):
        self._last_name = new_last_name
    
    @property
    def pesel(self):
        return self._pesel
    @pesel.setter
    def pesel(self, new_pesel):
        self._pesel = new_pesel
    
    @property
    def account_balance(self):
        return self._account_balance
    @account_balance.setter
    def account_balance(self, new_account_balance):
        self._account_balance = new_account_balance
    
    def deposit(self, money):
        '''a function that allows to deposit money into account balance'''
        self.account_balance += money
    
    def take_money(self, money):
        '''a function that allows you to take out money from account'''
        self.account_balance -= money
    
    def blik(self):
        '''a function generating random blik code'''
        blik_number = []
        i = 0
        while i <= 6:
            blik_number.append(random.randint(0, 9))
            i += 1
        return blik_number
    
    def buy(self, cost):
        '''a function that allows to buy smth using a bank acc '''
        if cost > self._account_balance:
            return 'insufficient funds on your acc'
        elif cost <= self._account_balance:
            self._account_balance -= cost


class SavingAccount(MainBankAccount):
    '''Saving account'''
    def __init__(self,saving_account_balance):#name, last_name, pesel, account_balance, saving_account_balance):
        #super(MainBankAccount, self).__init__(name, last_name, pesel, account_balance)
        self._saving_account_balance = saving_account_balance

    @property
    def saving_account_balance(self):
        return self._saving_account_balance
    @saving_account_balance.setter
    def saving_account_balance(self, new_saving_account_balance):
        self._saving_account_balance = new_saving_account_balance


    def deposit_to_saving_account(self, money):
        self._saving_account_balance += money
    
    def take_money_from_saving_account(self, money):
        if money > self._saving_account_balance:
            return 'insufficient funds on your acc'
        elif money <= self._saving_account_balance:
            self._saving_account_balance -= money

    def deposit_saving_account_from_main_account(self, money):
        pass


#test:


user1 = MainBankAccount('Karol', 'Walczak', 999999999, 10000)
print(user1.name)
print(user1.last_name)
print(user1.pesel)
print(user1.account_balance)
print(user1.blik())
user1.deposit(500)
print(user1.account_balance)
user1.take_money(1500)
print(user1.account_balance)
print(user1.buy(20000))
user1.buy(4000)
print(user1.account_balance)

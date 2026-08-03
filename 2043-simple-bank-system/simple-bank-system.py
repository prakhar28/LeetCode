class Bank:

    def __init__(self, balance: List[int]):
        self.balances = balance
        self.accounts = len(balance)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.isValid(account1) and self.isValid(account2) and self.balances[account1 - 1] >= money:
            self.balances[account1- 1] = self.balances[account1- 1] - money
            self.balances[account2- 1] = self.balances[account2- 1] + money
            return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if not self.isValid(account):
            return False
        self.balances[account- 1] = self.balances[account- 1] + money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        print("account, money", account, money)
        print("balances", self.balances)
        if not self.isValid(account) or self.balances[account- 1] < money:
            return False
        self.balances[account- 1] = self.balances[account- 1] - money
        return True
    
    def isValid(self, account):
        if account - 1 < self.accounts:
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
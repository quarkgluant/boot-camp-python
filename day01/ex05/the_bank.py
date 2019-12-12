#!/usr/bin/env python3
# -*-coding:utf-8 -*


class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
            Account.ID_COUNT += 1
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank
        Now you have to code the class Bank.
        It will have to handle the security part of each transfer attempt.
        Security means checking if the Account is:
            • the right object
            • that it is not corrupted
            • and that it has enough money
        How do we define if a bank account is corrupted ?
            • It has an even number of attributes.
            • It has an attribute starting with b.
            • It has no attribute starting with zip or addr.
            • It has no attribute name, id and value.
        A transaction is invalid if amount < 0 or if the amount is larger than the funds the first
        account has available for transfer.
    """
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest:
            int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return
            True if success, False if an error occured
        """

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return
            True if success, False if an error occured
        """
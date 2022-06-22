"""
Module describes class User with next parameters: name, surname,
adressbook
"""
from address_book import AddressBook


class User:
    """
    Class for instance of user
    """
    def __init__(self, name, surname, adress_book: AddressBook):
        self.name = name
        self.surname = surname
        self.adress_book = adress_book

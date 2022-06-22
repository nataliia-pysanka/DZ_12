"""
Module describes class Record with next parameters: name, list of phones
"""
import json
import datetime
from typing import Union, List

from field import Name, Phone, Birthday


class Record:
    """
    Class for instance Record
    """

    def __init__(self, name: Name,
                 phone: Phone = None,
                 birthday: Birthday = None):
        self._numbers = []
        self._name = None
        self._birthday = None
        if name:
            self.name = name
        if phone:
            self._numbers.append(phone)
        if birthday:
            self.birthday = birthday

    @property
    def name(self):
        return self._name.value

    @name.setter
    def name(self, new_name: Name):
        self._name = new_name

    @property
    def birthday(self):
        if self._birthday:
            return self._birthday.value
        return 'No data'

    @property
    def birthday_as_date_type(self):
        return self._birthday.value_as_date_type

    @birthday.setter
    def birthday(self, new_birthday: str):
        self._birthday = new_birthday

    @property
    def numbers(self):
        if self._numbers is not None:
            return self._numbers

    def days_to_birthday(self):
        birthday = self.birthday_as_date_type
        if birthday:
            today = datetime.datetime.now()
            if today.month >= birthday.month and today.day > birthday.day:
                year = today.year + 1
            else:
                year = today.year
            date_birth = datetime.datetime(year=year,
                                           month=birthday.month,
                                           day=birthday.day)
            date_today = datetime.datetime(year=today.year,
                                           month=today.month,
                                           day=today.day)
            if year > today.year:
                delta = date_birth - date_today
            else:
                delta = date_today - date_birth
            return f'Days to birthday: {abs(delta.days)}'

    def __str__(self):
        rec = '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
        rec += '\t {:<8} : {:<15}'.format('Name', self.name) + '\n'
        rec += '\t {:<8} : {:<15}'.format('Birthday', self.birthday) + '\n'
        rec += '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
        for number in self.numbers:
            rec += '\t {:<8} : {:<15}'.format('Number', number.value) + '\n'
        rec += '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
        return rec

    def append_number(self, number: Phone):
        """
        Function append new Phone object to the list of phones
        """
        # print('Adding a new number...')
        if not isinstance(number, Phone):
            # print('\t It should be a Phone object')
            # print("Can't add this number \n")
            return False

        if number in self.numbers:
            print(f'\t The number {number} already exist \n')
            return False

        self.numbers.append(number)
        # print(f'\t The number {number} was added \n')
        return True

    @staticmethod
    def edit_number(self, edit_number: Phone, new_number: str):
        """
        Function edit Phone object
        """
        print(f'Editing {edit_number}...')
        if not isinstance(edit_number, Phone):
            print('\t It should be a Phone object')
            print("Can't edit this number \n")
            return False
        if edit_number.edit(new_number):
            print(f'\t Number {edit_number} was changed \n')
            return True
        print(f"\t Number {edit_number} wasn't changed \n")
        return True

    def delete_number(self, del_number: Phone):
        """
        Function delete Phone object from the list of phones
        """
        print(f'Deleting {del_number}...')
        if not isinstance(del_number, Phone):
            print('\t It should be a Phone object')
            print("Can't delete this number \n")
            return False
        if del_number in self.numbers:
            index = self.numbers.index(del_number)
            self.numbers.pop(index)
            print(f'\t The number {del_number} was deleted \n')
            return True
        print(f'\t No number {del_number} in the book')
        return False

    def serealize(self):
        dump = {'name': self.name}
        if self.birthday:
            dump.update({'birthday': self.birthday})
        numbers = []
        for number in self.numbers:
            numbers.append(number.value)
        dump.update({'numbers': numbers})
        return dump

    def deserealize(self, record):
        self.name = Name(record['name'])
        self.birthday = Birthday(record['birthday'])
        numbers = record['numbers']
        for number in numbers:
            self.append_number(Phone(number))

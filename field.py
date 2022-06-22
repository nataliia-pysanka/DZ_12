"""
Module describes class Field
"""
from abc import ABC, abstractmethod
from re import findall as re_search
from datetime import datetime, date


class Field(ABC):
    """Abstract class for fields in records of adress book"""
    @property
    @abstractmethod
    def value(self):
        raise NotImplementedError

    @value.setter
    @abstractmethod
    def value(self, new_value):
        raise NotImplementedError


class Name(Field):
    """
    Class Name
    """
    def __init__(self, value):
        self._value = None
        self.edit(value)

    @property
    def value(self):
        if self._value:
            return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            self._value = 'No name'

    def __str__(self):
        return self.value

    def edit(self, new_value: str):
        """
        Function for editing value of Name
        :param new_value: str
        :return: boolean
        """
        try:
            self.value = new_value
        except ValueError as err:
            print(err)
            return False
        return True


class Phone(Field):
    """
    Class Phone
    """
    def __init__(self, number):
        self._value = 'No number'
        self.edit(number)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError('Number should be a string \n')
        search = re_search('\D', new_value)
        if 10 <= len(new_value) <= 15 and len(search) == 0:
            self._value = new_value
        else:
            raise ValueError('\t Length of number should be 10-15 symbols')

    def __str__(self):
        return self.value

    def edit(self, new_value: str):
        """
        Function for editing value of Phone
        :param new_value: str
        :return: boolean
        """
        try:
            self.value = new_value
        except ValueError as err:
            print(err)
            return False
        return True


class Birthday(Field):
    def __init__(self, birth: str):
        self._value = None
        self.edit(birth)

    @property
    def value(self):
        if self._value:
            return self._value.strftime('%Y-%m-%d')

    @property
    def value_as_date_type(self):
        if self._value:
            return self._value

    @value.setter
    def value(self, new_value):
        self._value = datetime.strptime(new_value, '%Y-%m-%d')

    def __str__(self):
        if self.value:
            return self.value
        return 'No birthday'

    def edit(self, new_value: str):
        """
        Function for editing value of Birthday
        :param new_value: str
        :return: boolean
        """
        try:
            self.value = new_value
        except ValueError as err:
            print(err)
            return False
        except TypeError as err:
            print(err)
            return False
        return True

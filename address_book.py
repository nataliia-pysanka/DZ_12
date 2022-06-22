from time import sleep
from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.names = []

    def add_record(self, rec: Record):
        key = rec.name
        self[key] = rec
        self.names.append(key)

    def __str__(self):
        res = ''
        for key in self.data:
            res += f'{key}\n'

        return res

    # def __iter__(self):
    #     for value in self.data.values():
    #         yield value
    #         self.counter += 1
    #         if self.counter == 3:
    #             input()
    #             self.counter = 0
    #     raise StopIteration

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < len(self.names):
            if self.counter > 0 and self.counter % 3 == 0:
                input()
            index = self.counter
            self.counter += 1
            return self.data[self.names[index]]

        self.counter = 0
        raise StopIteration

    def print(self):
        for rec, data in self.data.items():
            print(data)



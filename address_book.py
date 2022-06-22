import json
from collections import UserDict
from record import Record


class AddressBook(UserDict):
    FILE_NAME = 'contacts.json'

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
        if len(self.data) > 1:
            for key in self.data:
                res += f'{key}\n'
        return res

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

    def save(self):
        dump = []
        for key, record in self.data.items():
            dump.append(record.serealize())
        with open(self.FILE_NAME, 'w', encoding='UTF-8') as file:
            json.dump(dump, file)

    def load(self):
        self.clear()
        with open(self.FILE_NAME, 'r', encoding='UTF-8') as file:
            dump = json.load(file)
        for record in dump:
            rec = Record('No name')
            rec.deserealize(record)
            self.add_record(rec)

    def clear(self):
        self.counter = 0
        self.names = []
        self.data = {}

"""
Main module
"""
from random import randint
from datetime import datetime
from faker import Faker
from address_book import AddressBook
from field import Phone, Name, Birthday
from record import Record

fake = Faker()


def fake_record():
    name = fake.first_name()
    date = fake.date_between(start_date='-70y', end_date='-15y')
    date_birth = datetime.strftime(date, '%Y-%m-%d')
    phone = str(fake.random_number(digits=randint(10, 15)))
    name = Name(name)
    phone = Phone(phone)
    birth = Birthday(date_birth)
    rec = Record(name=name, phone=phone, birthday=birth)
    for _ in range(2):
        phone = str(fake.random_number(digits=randint(11, 13)))
        rec.append_number(Phone(phone))
    return rec


if __name__ == '__main__':
    book = AddressBook()
    book.load()
    book.clear()
    for record in book:
        print(record)
    book.add_record(fake_record())
    for record in book:
        print(record)

from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record] = record


class Record:
    record = dict()

    def __init__(self, name, phone):
        self.record[f"{name}"] = phone
        self.name = name
        self.phones = []


    def add_phone(self, phone):
        self.phones = phone

    def remove(self, name):
        self.phones.pop(name)

    def edit_phone(self, phone):
        pass


class Field:
    pass


class Name(Field):

    def __init__(self, name):
        self.name = name


class Phone(Field):

    def __init__(self, phone):
        self.phone = phone

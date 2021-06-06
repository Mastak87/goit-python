from collections import UserDict
from datetime import datetime
import pickle


class AddressBook(UserDict):
    def add_record(self, name, record):
        self.data[name] = record

    def __iter__(self):
        return Record()


class Record:
    record = dict()
    MAX_VALUE = 5

    def __init__(self, name, phone, birthday = None):
        self.record[name] = phone
        self.name = Name(name)
        self.phones = Phone(phone)
        self.birthday = Birthday(birthday)
        self.current_value = 0
        self.data = AddressBook()

    def __next__(self, name, phone, birthday):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.data.items()
        raise StopIteration

    def add_user(self,name, phone, birthday = None):
        if name not in self.record:
            self.record[name] = phone
            self.name = Name(name)
            self.phones[name] = Phone(phone)
            self.birthday = Birthday(birthday)

    def add_phone(self, name, phone):
        self.phones.phones.append(phone)
        self.record[name] = self.phones.phones

    def remove(self, index):
        del self.phones.phones[index]

    def add_birthday(self,birthday):
        self.record['birthday'] = self.birthday

    def days_to_birthday(self, birthday):
        birthday= birthday.split('.')
        birthday = datetime(year=datetime.now().year, month=int(birthday[1]), day=int(birthday[0]))
        year = datetime(year=datetime.now().year, month=12, day=31)
        if birthday:
            date = birthday - datetime.now()
            if date.days > 0:
                return date.days
            else:
                date = birthday - datetime.today()
                return date.days + year.timetuple().tm_yday


class Field:
    def __str__(self):
        print(f"{self.__dict__}")


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    phones = list()

    def __init__(self, phone):
        self.phones.append(phone)
        self.phone = phone

    @property
    def value(self):
        return self.phone

    @value.setter
    def value(self, new_value):
        if new_value.isdigit():
            self.phone = new_value
        else:
            print('Only numbers accepted')


class Birthday:
    birthday =  dict()

    def __init__(self, birthday):
        self.birthday['birthday'] = birthday

    @property
    def value(self):
        return self.birthday

    @value.setter
    def value(self, new_value):
        for i in new_value.split('.'):
            if i.isdigit():
                self.birthday['birthday'] = new_value
            else:
                print('Enter your birthday,like in example "01.01.1970"')


class Reader:
    def __init__(self, file):
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def close(self):
        self.fh.close()

    def read(self, size=1):
        data = self.fh.read(size)
        self.position = self.fh.tell()
        return data

    def __getstate__(self):
        attributes = {**self.__dict__}
        attributes['fh'] = None
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.fh = open(value['file'])
        self.fh.seek(value['position'])
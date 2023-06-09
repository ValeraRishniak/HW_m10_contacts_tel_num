from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name : Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if isinstance(phone, Phone):
            self.phones.append(phone)


    #додавання контакту
    def add_phone_num(self, phone):
        self.phones.append(phone)


    #видалення контакту
    def delete_phone_num(self, phone):
        for seq_num, i in enumerate(self.phones):
            if i == phone:
                self.phones.pop(seq_num)


    #редагування контакту
    def change_phone_num(self, old_phone, new_phone):
        for seq_num, i in enumerate(self.phones):
            if i == old_phone:
                self.phones[seq_num] = new_phone


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record



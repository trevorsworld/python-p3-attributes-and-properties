#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    def set_name(self, name):
        if (isinstance(name, str)) and (1 <= len(name) <= 25):
            print(f"Breed must be in list of approved breeds.")
            self._name = name.title()
        elif name == False:
            print('Name must be string between 1 and 25 characters.')

        else:
            print('Name must be string between 1 and 25 characters.')
    name = property(get_name, set_name)  
    pass

snoop=Dog("snoop")
print(snoop.name)
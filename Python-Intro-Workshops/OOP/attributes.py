#!/usr/bin/python3
# ATTRIBUTES

class Cat(): 

    def __init__(self, name): 
        self.name = name

# pass an attribute to an instance object
missy = Cat('Missy')
lucky = Cat('Lucky')

print(missy.name)
print(lucky.name)
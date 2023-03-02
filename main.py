#!/usr/bin/env python

# -------------------------------------------------------------------------------------------------
# Version    : 1.0
# Date       : 24-FEB-2023
#--------------------------------------------------------------------------------------------------
import os
import json
#import requests
import re

class ExampleClass:
    def __init__(self, name):
        self._name = name
    
    def greet(self):
        return "Hello, my name is {}.".format(self.name)
    
    def farewell(self):
        return "Goodbye from {}!".format(self.name)
    
    @property
    def name(self):
        return self._name.title()
    # The title() method is a built-in string method in Python that returns a copy of the string 
    # with the first letter of each word capitalized and the rest of the letters in lowercase. 

if __name__ == '__main__':
    # Example usage
    my_instance = ExampleClass('Alice')
    print(my_instance.greet())
    print(my_instance.farewell())
    print(my_instance.name)  # Using the property
    print()
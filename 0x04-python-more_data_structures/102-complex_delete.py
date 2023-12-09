#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del a_dictionary[filter(lambda x: x == value, a_dictionary)]
    return a_dictionary

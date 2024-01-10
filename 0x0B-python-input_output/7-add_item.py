#!/usr/bin/python3
"""
Module add item JSON
"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
my_list = []
try:
    my_list = load_from_json_file(filename)
except Exception as ex:
    print(ex)
my_list.append(sys.argv)
try:
    save_to_json_file(my_list, filename)
except Exception as ex:
    print(ex)

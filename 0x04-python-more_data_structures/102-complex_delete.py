#!/usr/bin/python3

# deletes keys with a specific value in a dictionary.
# If the value doesn’t exist, the dictionary won’t change
# All keys having the searched value have to be deleted

def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_dict in list_keys:
        if value == a_dictionary.get(value_dict):
            del a_dictionary[value_dict]

    return (a_dictionary)

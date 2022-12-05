#!/usr/bin/python3

# a function that returns a tuple with
# the length of a string and its first character.
# If the sentence is empty, the 1st character = None

def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

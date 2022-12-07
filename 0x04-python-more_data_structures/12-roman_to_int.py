#!/usr/bin/python3

# converts a Roman numeral to an integer.
# assume the number will be between 1 to 3999.
# If the roman_string is not a string or None, return 0

def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) != str):
        return 0

    result = 0
    vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    limit = len(roman_string)
    for ch in range(0, limit):
        if ch == len(roman_string) - 1:
            result += vals[roman_string[ch]]
        elif vals[roman_string[ch]] >= vals[roman_string[ch + 1]]:
            result += vals[roman_string[ch]]
        else:
            result -= vals[roman_string[ch]]
    return result

#!/bin/python3

import math
import os
import random
import re
import sys


def sortRoman(names):
    names = ['Louis IX', 'Louis VII', 'Louis XXII']
    result = delimitSuffix(names)
    return result
    
def delimitSuffix(names):
    sorted_names = []
    for name in names:
        suffix = name.split(" ")[1]
        last_name = name.split(" ")[0]
        foobar = name.split(" ")[1]
        n=convertRoman(suffix); #n becomes 10
        last_name = last_name + " " + str(n)
        sorted_names.append(last_name)
    
    sorted_names.sort()
    #new_sorted_names = sorted(sorted_names, key=lambda x: x.split(" ")[1], reverse=True)
    new_sorted_names = sorted_names.sort(key=natural_keys)
    print('new_sorted', new_sorted_names)
    return new_sorted_names


def convertRoman(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val

if __name__ == "__main__":
    sortRoman('')
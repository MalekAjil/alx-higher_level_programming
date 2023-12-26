#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str) or n < 0:
        return str
    str2 = list(str)
    str2[n] = ''
    str3 = ''.join(str2)
    return str3

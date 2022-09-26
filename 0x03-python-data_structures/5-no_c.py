#!/usr/bin/env python3
def no_c(my_string):
    s = []
    new_str = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        s.append(i)
    return new_str.join(s)

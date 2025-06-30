# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:34:43 2022

@author: ADMIN
"""

s="Navanitha sri"
print(s)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count('i'))
print(s.endswith('ri'))
print(s.startswith('Na'))
print(s.find('i'))
print(s.find('i',6))
print(s.replace('i','e'))
print("is upper:",s.isupper())
print("is lower:",s.islower())
a="joes123"
print("Is Alpha Numeric:",a.isalnum())
print("Is Alpha:",a.isalpha())
b="he\nis\ngood"
print(b)
print(b.splitlines())
print(b.splitlines(True))
c="navanitha computer educatiion"
print(c.split(' '))
s="     nava    "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))
s="31-10-2022"
print(s.partition('-'))
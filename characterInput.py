#! /usr/bin/env python3
# characterInput.py - practicepython.org

name = input('Hello there, pray tell what is your name?\n')
age = int(input(('Thank you ' + name + '. And your happy age?\n')))
year = str((100 - age) + 2018)
print('You will turn 100 in the year ' + year + ' !')

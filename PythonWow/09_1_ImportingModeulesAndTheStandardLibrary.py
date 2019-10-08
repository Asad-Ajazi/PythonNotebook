# for illustration purposes purposes modules won't all be at the top of file

# importing my own module. AVOID starting with numbers, _ used here.
# as keyword to alias the module
import _09_2_my_module as mm

# direct function import (alias possible, as x)
# this method only give access to the find_index function and nothing else.
# can add extras
from _09_2_my_module import find_index, test
# from _09_2_my_module import * <-- Don't do this. hard to find what module things came from

print(test)

courses = ['English', 'Maths', 'Science', 'History']

# direct import to use find_index
index = find_index(courses, 'Science')
print(index)

# using alias mm with standard import
index = mm.find_index(courses, 'History')
print(index)

# sys.path shows all the directories python searches for modules in.
# order: directory containing running script -> python PATH environment ->
# the standard library -> site packages directory (3rd party)
# if directory is elsewhere, can use.
# sys.path.append('location') <-- bad
# or manually add it to path environment variables.
import sys
print(sys.path)

# next is the standard library (use these, they're efficient)
# to get a random value from the list
import random
random_course = random.choice(courses)
print(random_course)

import math
# convert degrees to radians
rads = math.radians(90)
print(math.sin(rads))
print()

import datetime
import calendar
# todays date
today = datetime.date.today()
print(today)

# checks for leap year
print(calendar.isleap(2019))
print(calendar.isleap(2020))
print()

# working with the os directly. files etc
import os
current_working_directory = os.getcwd()
print(current_working_directory)

# find location of os module. directory
print(os.__file__)
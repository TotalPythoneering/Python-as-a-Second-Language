# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-23 06:30:21
# FILE: nollamas.py
# AUTHOR: Randall Nagy
#
name = input("Name: ")
print("Welcome, '", name, "'!")
try:
    age = input('Age: ')
    iage = int(age)
    print("Got:", name, iage)
except ValueError:
    print('Age is not numeric')


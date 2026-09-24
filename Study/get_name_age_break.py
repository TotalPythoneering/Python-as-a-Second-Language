# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2022-04-12 10:30:33
# FILE: get_name_age_break.py
# AUTHOR: Randall Nagy
#
def get_name_age():
    name = input("Name: ")
    print("Welcome, '", name, "'!")
    while True:
        try:
            age = input('Age: ')
            iage = int(age)
            break # return name, iage
        except ValueError:
            print('Age is not numeric')
    return name, iage


if get_name_age():
    print("Welcome!")
else:
    print("Error.")

    


# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-27 03:57:36
# FILE: get_name_age_if.py
# AUTHOR: Randall Nagy
#
def get_name_age():
    name = input("Name: ")
    try: 
        return name, int(input('Age: '))
    except ValueError:
        pass


if get_name_age():
    print("Welcome!")
else:
    print("Error.")

    


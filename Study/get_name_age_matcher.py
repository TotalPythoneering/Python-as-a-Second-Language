# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-27 03:46:28
# FILE: get_name_age_matcher.py
# AUTHOR: Randall Nagy
#

match int(input('Age: ')):
    case 0|1|2|3|4|5|6|7|8:
        print("Ride a Trike")
    case 9|10|11|12|13|14|15|16:
        print("Get a Bike")
    case _:
        print("Try a Motorized Vehicle!")



        


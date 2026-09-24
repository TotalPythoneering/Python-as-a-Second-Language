# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-23 07:50:52
# FILE: get_name_age.py
# AUTHOR: Randall Nagy
#
def get_name_age():
    name = input("Name: ")
    try: 
        return name, int(input('Age: '))
    except ValueError:
        pass

results = get_name_age()
if not results:
    print("Bad input...")
elif results[1] < 8:
    print("Ride a Trike")
elif results[1] < 16:
    print("Get a Bike")
else:
    print("Try a Motorized Vehicle!")


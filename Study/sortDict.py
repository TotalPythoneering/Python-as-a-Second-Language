# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-23 09:49:01
# FILE: sortDict.py
# AUTHOR: Randall Nagy
#
def sort(row):
    return len(row)

data = {"First":"John",
        "Last":"Doe",
        "Phone":"123-456-7890",
        "Email":"foo@bar.net"}

keys = list(data.keys())
keys.sort(key=sort)

for key in keys:
    print(f"{key:>10s}:[{data[key]:20s}]")



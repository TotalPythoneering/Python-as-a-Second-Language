# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-23 10:34:45
# FILE: FormatPcts.py
# AUTHOR: Randall Nagy
#
data = {"First":"John",
        "Last":"Doe",
        "Phone":"123-456-7890",
        "Email":"foo@bar.net"}

for key in data:
    print("%10s:[%-20s]" % (key, data[key]))



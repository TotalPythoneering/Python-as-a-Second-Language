# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-29 10:01:38
# FILE: exmut75.py
# AUTHOR: Randall Nagy
#
data = dict()

def update(adict):
    if isinstance(adict, dict):
        adict['ok'] = True


update(data)
print(data)


# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-25 04:59:22
# FILE: ListOne.py
# AUTHOR: Randall Nagy
#
data = "Fun", "Pun", "Run", "Sun"
for line in data:
    print(line)

data = ["Fun", "Pun", "Run", "Sun"]
for ss, line in enumerate(data, 1):
    if ss % 4 == 0:
       print()
    print(line, '\t', end='')

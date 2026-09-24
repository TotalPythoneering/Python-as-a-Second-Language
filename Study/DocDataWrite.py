# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-23 09:19:35
# FILE: DocDataWrite.py
# AUTHOR: Randall Nagy
#
data = '''
One
Two Three
Four
'''

with open("DocData.txt", 'w') as fh:
    print(data, file=fh)

with open("DocData.txt") as fh:
    print(*fh)

with open("DocData.txt") as fh:
    for ss, line in enumerate(fh, 1):
        print(ss, line, sep = '.) ')


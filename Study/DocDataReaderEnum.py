# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-23 09:25:55
# FILE: DocDataReaderEnum.py
# AUTHOR: Randall Nagy
#
data = '''\nOne\nTwo\nThree\nFour\n\n\n'''

with open("DocData.txt", 'w') as fh:
    print(data, file=fh)

with open("DocData.txt") as fh:
    for ss, line in enumerate(fh):
        if line.strip() != '':
            print(ss, line, sep = '.) ', end='')



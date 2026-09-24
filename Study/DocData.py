# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-23 09:08:17
# FILE: DocData.py
# AUTHOR: Randall Nagy
#
data = '''
One
Two Three
Four
'''

for line in data.split():
    print(line)

for line in data.split('\n'):
    print(line)


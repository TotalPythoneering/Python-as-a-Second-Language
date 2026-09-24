# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-27 08:35:46
# FILE: Act95.py
# AUTHOR: Randall Nagy
#
def read_strings()->list:
    results = []
    while True:
        _str = input("Row: ").strip()
        if not _str:
            return results
        results.append(_str)

MAX_WIDE = 72            
def mainloop():
    values = read_strings()
    _len = 0; screen_width = 0;
    for value in values:
        _len = max(len(value), _len)
    _len += 1
    for value in values:
        zcol = f"{value.ljust(_len)}"
        screen_width += len(zcol)
        if screen_width > MAX_WIDE:
            print();screen_width = len(zcol)
        print(zcol, end='')

mainloop()   



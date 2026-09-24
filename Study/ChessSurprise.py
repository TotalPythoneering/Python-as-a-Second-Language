# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-11-01 06:02:03
# FILE: ChessSurprise.py
# AUTHOR: Randall Nagy
#
from collections import OrderedDict as OrderedDict           
pieces = OrderedDict()
pieces['sp'] = '☐'
pieces['wK'] = chr(9812)
pieces['wq'] = chr(9813)
pieces['wc'] = chr(9814)
pieces['wb'] = chr(9815)
pieces['wk'] = chr(9816)
pieces['wp'] = chr(9817)
pieces['bK'] = chr(9818)
pieces['bq'] = chr(9819)
pieces['bc'] = chr(9820)
pieces['bb'] = chr(9821)
pieces['bk'] = chr(9822)
pieces['bp'] = chr(9823)

for char in range(9812, 9824):
    print(chr(char), end='')
print(chr(9744))

def get_row(is_odd, keys=None)->str:
    results = ''
    for col in range(1, 9):
        piece = ' '
        if keys and len(keys) == 8:
            piece = pieces[keys[col-1]]
        if col % 2 == 0:
            if is_odd:
                results += f"[{piece}]"
            else:
                results += f" {piece} "
        else:
            if is_odd:
                results += f" {piece} "
            else:
                results += f"[{piece}]"
    return results

def chess_board():
    for row in range(1, 9):
        is_odd = row%2 != 0
        if row == 1:
            print(get_row(is_odd, ['wc','wk','wb', 'wK','wq','wb','wk','wc']))
        elif row == 2:
            print(get_row(is_odd, ['wp','wp','wp','wp','wp','wp','wp','wp']))
        elif row == 7:
            print(get_row(is_odd, ['bp','bp','bp','bp','bp','bp','bp','bp']))
        elif row == 8:
            print(get_row(is_odd, ['bc','bk','bb', 'bK','bq','bb','bk','bc']))
        else:
            print(get_row(is_odd, ['sp','sp','sp','sp','sp','sp','sp','sp']))

chess_board()   



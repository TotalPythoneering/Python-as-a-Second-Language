# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-11-01 06:21:49
# FILE: ActChessBoard.py
# AUTHOR: Randall Nagy
#
pieces = dict()
pieces['sp'] = '☐'
pieces['wK'] = "♔"
pieces['wq'] = "♕"
pieces['wb'] = "♗"
pieces['wk'] = "♘"
pieces['wc'] = "♖"
pieces['wp'] = "♙"
pieces['bK'] = '♚'
pieces['bq'] = '♛'
pieces['bb'] = '♝'
pieces['bk'] = '♞'
pieces['bc'] = '♜'
pieces['bp'] = '♟'

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
            print(get_row(is_odd, \
                ['wc','wk','wb', 'wK','wq','wb','wk','wc']))
        elif row == 2:
            print(get_row(is_odd, \
                ['wp','wp','wp','wp','wp','wp','wp','wp']))
        elif row == 7:
            print(get_row(is_odd, \
                ['bp','bp','bp','bp','bp','bp','bp','bp']))
        elif row == 8:
            print(get_row(is_odd, \
                ['bc','bk','bb', 'bK','bq','bb','bk','bc']))
        else:
            print(get_row(is_odd, \
                ['sp','sp','sp','sp','sp','sp','sp','sp']))

if __name__ == '__main__':
    chess_board()   



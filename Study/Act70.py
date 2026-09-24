# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# as a Second Language.''
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-as-a-Second-Language
# DATE: 2021-10-27 07:14:37
# FILE: Act70.py
# AUTHOR: Randall Nagy
#
def the_report(zstring):
    print(f"Length: {len(zstring)}");
    print(f"That size is ", end='')
    if(len(zstring)%2==0):
        print("even.")
    else:
        print("odd.")

def mainloop():
    while True:
        astring = input("Enter String: ")
        the_report(astring)
        ztest = input("Continue? [N/y] ").strip().lower()
        if not ztest or ztest[0] != 'y':
            print("Goodbye!")
            return

mainloop()   


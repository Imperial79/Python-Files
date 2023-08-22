'''
2. Write a script that accepts two command line arguments and checks that exactly two
command line arguments are passed, no less or no more, and that the first argument is an
integer and the second is a string. Make useful feedback if they are not.
[To read command line arguments import sys and use sys.argv[ ]

Or,

import argparse and use parse_args() of ArgumentParser() ]
'''

import sys
n = len(sys.argv)
if n == 3:
    if sys.argv[1].strip().isdigit():
        if not(sys.argv[2].strip().isdigit()):
            print("All input are perfact...")
        else:
            print("2nd Argument is not String..")
    else:
        print("1st argument is not Integer..")

else:
    print("Number of arguments are passed, no less or no more than two")

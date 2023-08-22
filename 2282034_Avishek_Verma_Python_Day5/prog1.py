''' 
1. Write a script that reads lines from a file, adds line numbers to them, and then stores the
numbered lines into a new file. The name of the input file and also the new file will be read
from the user. Each line in the output file should begin with the line number, followed by a
colon and a space, followed by the line from the input file. 
'''

x = "#"  # Prog1
"""prog1"""
fName = input(
    "Enter the name of the input file (existing): ")  # input of filepath
rfile = open(fName, 'r')
r = rfile.readlines()
fName2 = input("Enter the name of the write file (new): ")

wfile2 = open(fName2, 'w')
for i in range(len(r)):
    wfile2.write(f'{i+1}: {r[i]}')
wfile2.close()

rfile2 = open(fName2, 'r')

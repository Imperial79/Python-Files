'''
3. Create a script that removes all of the comments from a Python source file and save the
modified file with a new name.
'''

flag = 0
rfile = open('prog1.py', 'r')
lst = rfile.readlines()
wfile2 = open('testProg.py', 'w')

lst2 = []
for i in lst:
    if flag == 1:
        if "'''" in i:
            # end of multiline'
            flag = 0

    else:
        if "'''" in i:
            # start of multiline'
            flag = 1
            if "'''" in i.replace("'''", "", 1):    # checking for single line multiline comment
                flag = 0
                lst2.append("")

        elif '#' in i:
            lst2.append('#'.join(i.split('#')[:-1]) + '\n')
            flag = 0
        else:
            lst2.append(i)

wfile2.writelines(lst2)
wfile2.close()

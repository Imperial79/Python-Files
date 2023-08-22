'''
2. Convert a Linux (UNIX) file permission in octal format into a string format.
[The permissions are split into three sets of three permissions: read, write, and execute for the
owner, group, and others. Each of the three values can be expressed as an octal number summing
each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or, it can be written with
a string using the letters r, w, and x or - when the permission is not granted]
Sample input Sample output
755     rwxr-xr-x
750     rwxr-x---
642     rw-r---w
'''
perm = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
result = ''
oct = input("Enter an octal value: ")
for i in oct:
    for j in i:
        result += perm[int(j)]

print(result)

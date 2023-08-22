'''Generate a string by rotating a given string by 'n' elements.
Sample Input: mca students n=2
Output: 
    Left Rotation: a studentsmc
    Right Rotation: tsmca studen
'''

line = line2 = input("Enter a line: ")
n = int(input("Enter value of n: "))
print("Right Rotation - "+line[-n:] + line[:-n])
print("Left Rotation - "+ line2[n:] + line[:n])




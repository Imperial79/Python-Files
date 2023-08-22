'''
16. Use lambda to sort a list of roll numbers by the last three digits of the roll number.
Sample Input: [20223005, 20222342, 20229000, 20220002, 20222345, 20229329]
Output: [20229000, 20220002, 20223005, 20229329, 20222342, 20222345]
'''

roll = [20223005, 20222342, 20229000, 20220002, 20222345, 20229329]

print(sorted(roll, key=lambda x: (str(x))[-3:]))

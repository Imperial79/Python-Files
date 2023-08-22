'''
15. Write a function that takes a string as a parameter and returns a list of the five most frequent characters in the string.
'''


def frequent(line):
    arr = []
    for ch in line:
        if ch not in arr:
            arr.append(ch)
        if len(arr) == 5:
            return arr
    return arr


print(frequent('AMMA'))

'''
12. Given a list of filenames, generate a new list to rename all the files with extension ‘cpp’ to the
extension ‘h’.
Sample Input: ["program.c", "stdio.cpp", "sample.cpp", "a.out", "math.cpp", "cpp.out"]
Output: ['program.c', 'stdio.h', 'sample.h', 'a.out', 'math.h', 'cpp.out']
'''

lst = ["program.c", "stdio.cpp", "sample.cpp", "a.out", "math.cpp", "cpp.out"]

print([i.replace('.cpp', '.h') for i in lst])

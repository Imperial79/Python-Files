grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
# grid = ['mpxz', 'abcd', 'wlmf']
size = len(grid)

for rw in range(size):
    temp = grid[rw]
    temp = list(temp)
    temp = sorted(temp)
    grid[rw] = ''.join(temp)

for j in range(size):
    grid[j] = list(grid[j])

row = size
col = len(grid[0])
arr = []
chk = []
flag = 0
for i in range(col):
    for j in range(row):
        arr.append(grid[j][i])
    chk = sorted(arr)
    if (arr != chk):
        flag = 1
        break
    else:
        arr = []
        chk = []
if (flag == 0):
    print('Yes')
else:
    print('No')

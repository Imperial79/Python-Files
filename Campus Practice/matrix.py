matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]]
row = []
col = []
sizeRow = len(matrix)
sizeCol = len(matrix[0])

for i in range(sizeRow):
    col.append(matrix[i][2])
col.reverse()


for i in range(sizeRow):
    matrix[i][2] = col[i]

for i in range(sizeCol):
    row.append(matrix[0][i])

row.reverse()

for i in range(sizeCol):
    matrix[0][i] = row[i]
sum = 0
for i in range(sizeRow):
    for j in range(sizeCol):
        if (i <= 1 and j <= 1):
            sum += (matrix[i][j])
print(sum)

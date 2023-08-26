# 8. Given an array of pairs, find all symmetric pairs in it. Two pairs (a, b) and (c, d) are said
# to be symmetric if c is equal to b and a is equal to d. For example, (10, 20) and (20, 10)
# are symmetric.
# Given an array of pairs find all symmetric pairs in it. It may be assumed that the first
# elements of all pairs are distinct.
# Input: arr[] = {{11, 20}, {30, 40}, {5, 10}, {40, 30}, {10, 5}}
# Output: Following pairs have symmetric pairs (30, 40) (5, 10)


arr = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]
out = []
visited = {1, }

for i in range(len(arr)):
    for j in range(1, len(arr)):
        if (set(arr[i]).issubset(set(arr[j])) and len(arr[i]) == len(arr[j]) and (i not in visited or j not in visited) and i != j):
            visited.add(i)
            visited.add(j)
            out.append(arr[i])
            break

print(out)

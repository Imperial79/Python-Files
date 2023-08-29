words = ["i", "love", "leetcode", "i", "love", "coding"]
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 2
k = 4
d = {}
for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

o = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print(list(o.keys())[:k])

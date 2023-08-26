# # Given an array of strings words and an integer k, return the k most frequent strings.
# # Return the answer sorted by the frequency from highest to lowest. Sort the words with
# # the same frequency by their lexicographical order.

arr = ['abc', 'bcd', 'ccd', 'ccd', 'abc', 'uid', 'uid']
d = {}
for i in arr:

    if (i in d):
        d[i] += 1
    else:
        d[i] = 1

srtd = sorted(d.keys(), key=lambda word: (d[word], word))
print(srtd[:2])

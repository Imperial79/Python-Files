'''
13. Given a dictionary, which contains domain names as keys, and a list of users as values, generate a list that contains complete email addresses.
Sample input ->
{"gmail.com": ["paul.buchheit", "sanjeev.singh", "kevin.fox"], "yahoo.com": ["jerry.yang", "david.filo"], "hotmail.com": ["sabeer.bhatia"]}
Sample output ->
['paul.buchheit@gmail.com','sanjeev.singh@gmail.com','kevin.fox@gmail.com', 'jerry.yang@yahoo.com', 'david.filo@yahoo.com', 'sabeer.bhatia@hotmail.com']

'''

d = {"gmail.com": ["paul.buchheit", "sanjeev.singh", "kevin.fox"], "yahoo.com": [
    "jerry.yang", "david.filo"], "hotmail.com": ["sabeer.bhatia"]}

for i in d:
    for j in d[i]:
        print(j + '@' + i)

'''
15. Consider the following data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
(i) create a pie chart of the popularity of programming Languages.
(ii) add a title.
(iii) make multiple wedges of the pie.
'''

import matplotlib.pyplot as plt
d = {
    'Java': 22.2,
    'Python': 17.6,
    'PHP': 8.8,
    'JavaScript': 8,
    'C#': 7.7,
    'C++': 6.7,
}

courses = list(d.keys())
values = list(d.values())
plt.pie(values, labels=courses)

plt.title('Programming Languages')
plt.show()

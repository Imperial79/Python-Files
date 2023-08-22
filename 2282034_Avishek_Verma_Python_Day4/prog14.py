'''
14. Given a dictionary as stated in the sample input, use lambda to
Sample Input: {"Kerala": ["Kannur", "Palakkad", "Thalassery"],
 "Maharastra": ["Bhandara", "Nagpur", "Wardha"],
 "West Bengal": ["Asansol", "Basirhat", "Tamluk"]}
(i) sort the states in order by the first city name. (['West Bengal', 'Maharastra', 'Kerala'])
(ii) sort the states by the length of the second city name, break ties of equal length by name of the second cities. (['Maharastra', 'West Bengal', 'Kerala'])
(iii) sort the states in order by the number of cities having length greater than 6.
(['Maharastra', 'Kerala', 'West Bengal'])

'''
d = {"Kerala": ["Kannur", "Palakkad", "Thalassery"],
     "Maharastra": ["Bhandara", "Nagpur", "Wardha"],
     "West Bengal": ["Asansol", "Basirhat", "Tamluk"]}


print('14 (i) ->', sorted(d, key=lambda x: d[x][0]))

print('14 (ii) ->', sorted(d, key=lambda x: (len(d[x][1]), d[x][1])))

print('14 (iii) ->', sorted(d, key=lambda x: len(d[x]) > 6))

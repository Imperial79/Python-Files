# 2. Given a time in 12hour AM/PM format, convert it to military (24-hour) time.Note: -
# 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.- 12:00:00PM on a 12-
# hour clock is 12:00:00 on a 24hour clock.
# Input : S = ’12:01:00PM’ Output: '12:01:00'
# Input : S = ’12:01:00AM’ Output: '00:01:00'
# Input : S = ‘07:05:45PM’Output: ‘19:05:45’


inp = "12:05:45AM"

temp = inp
annot = temp[8:]

dateList = temp[:-2].split(':')
hr, min, sec = (dateList[0]), (dateList[1]), (dateList[2])

print(hr, min, sec)

if (annot == "AM" and hr == '12'):
    hr = '00'
elif (annot == "PM" and int(hr) >= 1 or int(hr) <= 11):
    hr = str(int(hr)+12)

print("After formatting")
print(hr, ':', min, ':', sec)

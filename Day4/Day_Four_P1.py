from datetime import datetime
import re
import sleep as sp

# 2d array to hold the lines from the file
arr = [[0 for x in range(2)] for y in range(1056)]
ids = [] # array to hold the ids

numbers = re.compile('\d+(?:\.\d+)?')# regex to strip the ids from the text

file = open('sleep.txt', 'r')

for i, line in enumerate(file):

    date = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M:%S')
    string = line[19:]
    if re.search("^Guard #[0-9]{3,4} begins shift$", string):
        id = numbers.findall(string)
        id = int(id[-1])
        if id not in ids:
            ids.append(id)

    arr[i][0] = date
    arr[i][1] = string


file.close()

arr = sorted(arr, key=lambda dates: dates[0])
sp.part_one(arr, ids)


# this was to convert the sorted array to a file
# i did this because i had a feeling that the sorted list
# would come in handy for the second part
'''file = open("sorted_sleep.txt", "w+")
for i in range(1056):
    line = str(arr[i][0]) + ' ' + arr[i][1]
    file.write(line)
file.close()'''

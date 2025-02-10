# Darius Vaiaoga, Reading files notes

import csv

with open('Notes/things.txt', 'r') as file:
    content = file.read()
    index = content.find('love')
    print(content[index:index+5])

with open('Notes/sample.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(f'Username: {row[0]}, Favorite Color: {row[1]}')
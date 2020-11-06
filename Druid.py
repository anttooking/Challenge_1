import csv 

with open('Class list.csv') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[3])

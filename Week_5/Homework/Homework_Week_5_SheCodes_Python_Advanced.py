import csv

filename = 'Week_5\Homework\data.csv'

with open(filename, 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    print(line['continent'])
 
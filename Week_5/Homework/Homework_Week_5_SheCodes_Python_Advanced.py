import csv

filename = 'Week_5\Homework\data.csv'

with open(filename, 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    continent = line['continent']
    year = line['year']
    population = line['population']
    
    
 
import csv

filename = 'data.csv'

with open(filename, 'r') as csvfile:
  reader - csv.DictReader(csvfile)
  
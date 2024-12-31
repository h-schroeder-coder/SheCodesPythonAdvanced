import csv

with open('customers.csv', 'r') as file:
  cs = csv.reader(file)

  for c in cs:
    id = c[0]
    f = c[2]
    l = c[3]
    e = c[9]
    print(f"Customer #{id}, {f} {l}, {e}")
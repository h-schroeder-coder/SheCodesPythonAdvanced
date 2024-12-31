import csv

import matplotlib.pyplot as plt

filename = 'Week_5\Homework\data.csv'

population_per_continent = {}



with open(filename, 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    continent = line['continent']
    year = line['year']
    population = line['population']
    
    if continent not in population_per_continent:
      population_per_continent[continent] = {'population': [], 'years': []}
    
    population_per_continent[continent]['population'].append(population)
    population_per_continent[continent]['years'].append(year)
    


  
    
plt.plot([1990, 2000, 2010, 2020], [0, 25000000, 30000000, 35000000], label="Population", marker='*', color='m')
plt.plot([10, 20, 30], [15000000, 30000000, 40000000], label ="Animal", marker='o', color='c')
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Populations Across Continents & Time")
plt.grid(True)
plt.show()
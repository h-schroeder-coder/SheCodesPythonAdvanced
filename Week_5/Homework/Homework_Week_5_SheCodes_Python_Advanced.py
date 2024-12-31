import csv

import matplotlib.pyplot as plt

def generate_population_dictionary_from_csv(filename):
  """
  Generate population dictionary from csv data and return a dictionary following the structure below
  {
    "Africa": { population: [100, 200, 300], years: [1990, 2000, 2010]}
    "Europe": { population: [100, 200, 300], years: [1990, 2000, 2010]}
  }
  """
  
  output = {}
  
  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
      continent = line['continent']
      year = int(line['year'])
      population = int(line['population'])
      
      if continent not in output:
        output[continent] = {'population': [], 'years': []}
      
      output[continent]['population'].append(population)
      output[continent]['years'].append(year)
      
    return output
  
  
def generate_population_plots_from_dictionary(population_dictionary):
  """
  Generate the population plots from a dictionary with one plot per continent
  """
  for continent in population_dictionary:
    years = population_dictionary[continent]['years']
    population = population_dictionary[continent]['population']
    plt.plot(years, population, label=continent, marker='*')

  plt.xlabel("Year")
  plt.ylabel("Population (in billion users)")
  plt.title("Internet Populations Across Continents & Time")
  plt.grid(True)
  plt.legend()
  plt.tight_layout()
  plt.show()


filename = 'Week_5\Homework\data.csv'

# Display internet population in plots
population_per_continent = generate_population_dictionary_from_csv(filename)
generate_population_plots_from_dictionary(population_per_continent)
   


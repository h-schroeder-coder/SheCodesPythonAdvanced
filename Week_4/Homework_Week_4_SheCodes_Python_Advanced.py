def calculate_total_population(populations):
  """calculates the total population given a list of countries and populations"""
  
  total_population = 0
  for location in populations: 
    population = int(location['population'])
    total_population = total_population + population
    
    return total_population
    
def calculate_rounded_total_population(total_population):
  """returns rounded total population in millions, rounded to one decimal point"""
  total_population_in_millions = total_population / 1000000
  rounded_total_population_in_millions = round(total_population_in_millions, 1)
  
  return rounded_total_population_in_millions


def display_rounded_total_population(rounded_total_population_in_millions):
  print(f"The total population is {rounded_total_population_in_millions} million people")

#initial data set
populations = [
  { 'country': "France", "population": "60000000"},
  { 'country': "Spain", "population": "50000000"},
  { 'country': "USA", "population": "30000000"},
  { 'country': "Australia", "population": "25000000"},
  { 'country': "Canada", "population": "38000000"},
]

# Display the total population such as, the total population is 203 million people

total_population = calculate_total_population(populations)
rounded_total_population_in_millions = calculate_rounded_total_population(total_population)
display_rounded_total_population(rounded_total_population_in_millions)








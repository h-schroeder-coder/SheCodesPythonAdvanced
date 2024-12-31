

















def calculate_total_population(populations_list):
  """
  Calculate total population based on a list of countries
  """
  total = 0
  for population in populations_list:
    total = total + int(population['population'])

  return total

def display_total_population(total):
  """
  Display total population, divided by 1 million
  """
  total_in_millions = round(total / 1000000)
  print(f"The total population is {total_in_millions} million people")

# Initial data set
populations = [
  { 'country': "France", "population": "60000000"},
  { 'country': "Spain", "population": "50000000"},
  { 'country': "USA", "population": "30000000"},
  { 'country': "Australia", "population": "25000000"},
  { 'country': "Canada", "population": "38000000"}
]

# Display the total population
total_population = calculate_total_population(populations)
display_total_population(total_population)